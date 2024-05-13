from django.db import models
from django.contrib.auth.models import User

class Turma(models.Model):
    nome=models.CharField(max_length=20)
    periodo=models.IntegerField()

class Aluno(models.Model):
    nome=models.CharField(max_length=30)
    matricula=models.CharField(max_length=10)
    turma=models.ForeignKey(Turma, on_delete=models.CASCADE)

class Professor(models.Model):
    nome=models.CharField(max_length=30)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Materia(models.Model):
    nome=models.CharField(max_length=30)

class Relation_TPM(models.Model):
    turma=models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor=models.ForeignKey(Professor, on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)

def TPM(id):
    tpm = Relation_TPM.objects.get(pk=id)
    if tpm:
        turma = Turma.objects.get(pk=tpm.turma_id)
        alunos = Aluno.objects.filter(turma_id=turma.id)
        materia = Materia.objects.get(pk=tpm.materia_id)
        return {'id': id, 'turma': turma, 'alunos': alunos, 'materia': materia}
