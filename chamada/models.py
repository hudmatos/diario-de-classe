from django.db import models
from turmas.models import Aluno, Materia

class Chamada(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    data = models.DateField()
    presente = models.BooleanField()
    