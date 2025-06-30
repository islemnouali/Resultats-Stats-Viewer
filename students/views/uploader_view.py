from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings
from PyPDF2 import PdfReader
from tabula.io import read_pdf
import re
import tempfile

def etudiant_list(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('pdf_file')
        if not uploaded_file:
            return render(request, 'upload_pdf.html', {'error': "Aucun fichier PDF n'a été téléchargé."})

        try:
            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
                for chunk in uploaded_file.chunks():
                    tmp_file.write(chunk)
                temp_pdf_path = tmp_file.name

            reader = PdfReader(temp_pdf_path)
            start_page = None
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text and "Résultats de la session" in text:
                    start_page = i + 1  # tabula is 1-indexed
                    break

            if start_page is None:
                raise ValueError("La phrase 'Résultats de la session' est introuvable dans le PDF.")

            total_pages = len(reader.pages)
            page_range = list(range(start_page, total_pages + 1))

            dfs = read_pdf(temp_pdf_path, pages=page_range, encoding='ISO-8859-1', multiple_tables=True, lattice=True)

            cleaned_tables = []

            for df in dfs:
                if not isinstance(df, pd.DataFrame) or df.empty:
                    continue

                group_name = "Introuvable"
                for col in df.columns:
                    match = re.search(r"Groupe d'enseignement\s*:\s*(.*)", str(col))
                    if match:
                        group_name = match.group(1).strip()
                        break

                df = df.dropna(how='all')

                custom_headers = [
                    "Code etudiant", "Nom et prénom", "Moyenne semestre 1", "Crédit semestre 1",
                    "Moyenne du semestre 2", "Crédit semestre 2",
                    "Moyenne générale", "Crédit total", "Résultat"
                ]
                if len(df.columns) != len(custom_headers):
                    continue

                def is_header_row(row, headers, threshold=0.7):
                    matches = sum(str(cell).strip().lower() in [h.lower() for h in headers] for cell in row)
                    return matches / len(row) >= threshold

                # Apply fixed headers
                df.columns = custom_headers

                # 🔍 Check if first row is a repeated header
                if is_header_row(df.iloc[0], custom_headers):
                    df = df[1:].reset_index(drop=True)

                mask = (df == pd.Series(df.columns, index=df.columns)).all(axis=1)
                df = df[~mask]
                
                df = df[df.isna().sum(axis=1) <= 3]

                df["Groupe"] = group_name

                cleaned_tables.append(df)

            if not cleaned_tables:
                raise ValueError("Aucune table PDF valide extraite.")

            final_df = pd.concat(cleaned_tables, ignore_index=True)
            print("Saved to session:", final_df.shape)
            request.session['etudiants_data'] = final_df.to_json(orient='records')
            request.session['etudiants_columns'] = final_df.columns.tolist()
            request.session.modified = True  # ✅ Force session save

            return render(request, 'etudiants.html', {
                'excel_data': final_df.values.tolist(),
                'columns': final_df.columns.tolist(),
                'import_success': False,
                'import_error': None,
            })

        except Exception as e:
            return render(request, 'upload_pdf.html', {'error': f"Erreur lors du traitement du PDF : {e}"})

        finally:
            # Clean up the temp file
            if os.path.exists(temp_pdf_path):
                os.remove(temp_pdf_path)

    return render(request, 'upload_pdf.html')
