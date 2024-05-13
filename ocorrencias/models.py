from django.db import models
from turmas.models import Turma, Materia 

class Ocorrencia(models.Model):
    titulo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=200)
    data = models.DateField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)


