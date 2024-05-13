from django.db import models

class Turma(models.Model):
    nome=models.CharField(max_length=20)
    periodo=models.IntegerField()

class Aluno(models.Model):
    nome=models.CharField(max_lenght=30)
    matricula=models.Charfield(max_lenght=10)
    turma=models.ForeignKey(Turma, on_delete=models.CASCADE)

class Professor(models.Model):
    nome=models.CharField(max_lenght=30)

class Materia(models.Model):
    nome=models.CharField(max_lenght=30)

class Relation_TPM(models.Model):
    turma=models.ForeignKey(Turma, on_delete=models.CASCADE)
    professor=models.ForeignKey(Professor, on_delete=models.CASCADE)
    materia=models.ForeignKey(Materia, on_delete=models.CASCADE)
    