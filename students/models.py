from django.db import models

# Create your models here.
class Etudiant(models.Model):
    studentId = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    moy1 = models.FloatField()
    credit1 = models.FloatField()
    moy2 = models.FloatField()
    credit2 = models.FloatField()
    moy_total = models.FloatField()
    credit_total = models.FloatField()
    resultat = models.CharField(max_length=50, default='En attente')
    group = models.CharField()