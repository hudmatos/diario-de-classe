from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from turmas.models import Relation_TPM, Turma, Aluno, Materia
from . models import Chamada
from datetime import date
from django.http import HttpResponse
import pdb

@login_required
def index(request,id):
    tpm = Relation_TPM.objects.get(pk=id)
    materia = Materia.objects.get(pk=tpm.materia_id)
    alunos = Aluno.objects.filter(turma_id=tpm.turma_id)

    if request.method == "POST" and not chamada_existe(materia):
        alunos_presentes = request.POST.getlist('check')
        alunos_faltantes = alunos.exclude(id__in=alunos_presentes)
        marcar_presenca(alunos_presentes, materia)
        marcar_falta(alunos_faltantes, materia)
        
        return redirect(f'/chamada/{id}/')
    
    elif request.method == "POST" and chamada_existe(materia):
        alunos_presentes = request.POST.getlist('check')

        presentes = Chamada.objects.filter(data=date.today(), materia_id=materia.id, aluno_id__in=alunos_presentes)
        faltantes = Chamada.objects.filter(data=date.today(), materia_id=materia.id).exclude(aluno_id__in=alunos_presentes)

        for aluno in presentes:
            aluno.presente = True
            aluno.save()

        for aluno in faltantes:
            aluno.presente = False
            aluno.save()
        
        return redirect(f'/chamada/{id}/')

    chamada = []
    for aluno in alunos:
        chamada.append({'presente': verificar_presenca(aluno, materia)})

    lista_presenca = zip(alunos,chamada)
    relacao = {'id': id, 'materia': materia,'chamada': lista_presenca, 'edit': chamada_existe(materia)}
    return render(request, 'index.html', {'relacao': relacao})


def marcar_presenca(list_id, materia):
    if list_id and materia:
        for id in list_id:
            chamada = Chamada(
                aluno_id = id, 
                materia_id = materia.id,
                data = date.today(),
                presente = True
            )
            chamada.save()


def marcar_falta(alunos, materia):
     if alunos and materia:
        for aluno in alunos:
            chamada = Chamada(
                aluno_id = aluno.id, 
                materia_id = materia.id,
                data = date.today(),
                presente = False
            )
            chamada.save()

def verificar_presenca(aluno, materia):
    presenca = Chamada.objects.filter(data=date.today(), materia_id=materia.id, aluno_id=aluno.id)
    if presenca and presenca[0].presente:
        return True
    
def chamada_existe(materia):
    chamada = Chamada.objects.filter(data=date.today(), materia_id=materia.id)
    if chamada.exists():
        return True
    return False
    