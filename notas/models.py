from django.db import models
from turmas.models import Aluno, Materia

class Nota(models.Model):
    nota_1 = models.FloatField(default=0.0)
    nota_2 = models.FloatField(default=0.0)
    media = models.FloatField(default=0.0)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

