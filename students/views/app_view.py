from students.models import Etudiant
from django.shortcuts import render
import os
import pandas as pd
from django.conf import settings
from django.db.models import Avg
from django.core.files.storage import default_storage
from PyPDF2 import PdfReader
import re
from tabula.io import read_pdf

from django.shortcuts import render
from django.db.models import Avg
import pandas as pd


def get_etudiants_df_from_session(request):
    data = request.session.get('etudiants_data')
    columns = request.session.get('etudiants_columns')
    if data and columns:
        df = pd.read_json(data, orient='records')
        df.columns = columns
        print("Reading from session: found data?", data is not None)

        return df
    return None


def etudiants_view(request):
    print("Session keys:", request.session.keys())

    df = get_etudiants_df_from_session(request)
    if df is None:
        print("⚠️ DataFrame is None")
        return render(request, 'general.html', {'error': "Aucune donnée disponible. Veuillez d'abord importer un fichier."})
   
    print("✅ Loaded DF from session:", df.shape)

    admis_count = df[df['Résultat'].str.lower().str.contains('admis', na=False)].shape[0]
    total_count = df.shape[0]
    failure_count = total_count - admis_count

    avg_credit = pd.to_numeric(df['Crédit total'], errors='coerce').mean()
    avg_moyenne = pd.to_numeric(df['Moyenne générale'], errors='coerce').mean()

    top_10 = df.sort_values(by='Moyenne générale', ascending=False).head(15)
    top_1 = top_10.iloc[0] if not top_10.empty else None

    context = {
        'etudiants': df.to_dict('records'),
        'admis_count': admis_count,
        'failure_count': failure_count,
        'total_count': total_count,
        'avg_credit': round(avg_credit, 2) if avg_credit else 0,
        'avg_moyenne': round(avg_moyenne, 2) if avg_moyenne else 0,
        'top_10': top_10.to_dict('records'),
        'top_1': top_1.to_dict() if top_1 is not None else None,
        'stats_data': {
            'admisCount': admis_count,
            'totalCount': total_count
        }
    }

    return render(request, 'general.html', context)


    
def semestre1_valide_count_view(request):
    df = get_etudiants_df_from_session(request)
    if df is None:
        return render(request, 'sem1.html', {'error': "Aucune donnée disponible."})

    df['Moyenne semestre 1'] = pd.to_numeric(df['Moyenne semestre 1'], errors='coerce')
    df['Crédit semestre 1'] = pd.to_numeric(df['Crédit semestre 1'], errors='coerce')

    valide_count = df[df['Moyenne semestre 1'] > 10].shape[0]
    total_count = df.shape[0]
    failure_count = total_count - valide_count

    valide_rate = (valide_count / total_count * 100) if total_count else 0
    failure_rate = 100 - valide_rate

    avg_credit1 = df['Crédit semestre 1'].mean()
    avg_moyenne1 = df['Moyenne semestre 1'].mean()

    top_10 = df.sort_values(by='Moyenne semestre 1', ascending=False).head(15)
    top_1 = top_10.iloc[0] if not top_10.empty else None

    context = {
        'etudiants': df.to_dict('records'),
        'valide_count': valide_count,
        'total_count': total_count,
        'failure_count': failure_count,
        'avg_credit1': round(avg_credit1, 2) if avg_credit1 else 0,
        'avg_moyenne1': round(avg_moyenne1, 2) if avg_moyenne1 else 0,
        'top_10': top_10.to_dict('records'),
        'top_1': top_1.to_dict() if top_1 is not None else None,
        'stats_data': {
            'valideCount': valide_count,
            'totalCount': total_count
        },
        'valide_rate': round(valide_rate, 2),
        'failure_rate': round(failure_rate, 2),
    }

    return render(request, 'sem1.html', context)


def semestre2_valide_count_view(request):
    df = get_etudiants_df_from_session(request)
    if df is None:
        return render(request, 'sem2.html', {'error': "Aucune donnée disponible."})

    df['Moyenne du semestre 2'] = pd.to_numeric(df['Moyenne du semestre 2'], errors='coerce')
    df['Crédit semestre 2'] = pd.to_numeric(df['Crédit semestre 2'], errors='coerce')

    valide_count = df[df['Moyenne du semestre 2'] > 10].shape[0]
    total_count = df.shape[0]
    failure_count = total_count - valide_count

    valide_rate = (valide_count / total_count * 100) if total_count else 0
    failure_rate = 100 - valide_rate

    avg_credit2 = df['Crédit semestre 2'].mean()
    avg_moyenne2 = df['Moyenne du semestre 2'].mean()

    top_10 = df.sort_values(by='Moyenne du semestre 2', ascending=False).head(15)
    top_1 = top_10.iloc[0] if not top_10.empty else None

    context = {
        'etudiants': df.to_dict('records'),
        'valide_count': valide_count,
        'total_count': total_count,
        'failure_count': failure_count,
        'avg_credit2': round(avg_credit2, 2) if avg_credit2 else 0,
        'avg_moyenne2': round(avg_moyenne2, 2) if avg_moyenne2 else 0,
        'top_10': top_10.to_dict('records'),
        'top_1': top_1.to_dict() if top_1 is not None else None,
        'stats_data': {
            'valideCount': valide_count,
            'totalCount': total_count
        },
        'valide_rate': round(valide_rate, 2),
        'failure_rate': round(failure_rate, 2),
    }

    return render(request, 'sem2.html', context)
