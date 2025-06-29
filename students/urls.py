from django.urls import path
from .views import app_view
from .views import uploader_view

urlpatterns = [
    path('', uploader_view.etudiant_list, name='upload_pdf'),               
    path('etudiants/', app_view.etudiants_view, name='etudiants'),  
    path('sem1/', app_view.semestre1_valide_count_view, name='sem1'),
    path('sem2/', app_view.semestre2_valide_count_view, name='sem2')
]

