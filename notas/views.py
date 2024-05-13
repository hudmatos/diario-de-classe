from django.shortcuts import render
from turmas.models import Relation_TPM, Aluno, Materia
from django.http import HttpResponse
from django.shortcuts import redirect
from . models import Nota
import pdb

def notas(request, id):
    tpm = Relation_TPM.objects.get(pk=id)
    alunos = Aluno.objects.filter(turma_id=tpm.turma_id)
    materia = Materia.objects.get(pk=tpm.materia_id)
    notas = Nota.objects.filter(materia_id=materia.id)
    
    if request.method == 'POST' and not nota_existe(request.POST.get('aluno-id'),materia):
        nota01 = float(request.POST.get('nota01'))
        nota02 = float(request.POST.get('nota02'))
        media = (nota01 + nota02) / 2
        aluno_id = int(request.POST.get('aluno-id'))

        nota = Nota(
            nota_1 = nota01,
            nota_2 = nota02,
            media = media,
            aluno_id = aluno_id,
            materia_id = materia.id
        )

        nota.save()

        return redirect(f'/notas/{id}/')
    
    elif request.method == 'POST' and nota_existe(request.POST.get('aluno-id'), materia):
        nota01 = float(request.POST.get('nota01'))
        nota02 = float(request.POST.get('nota02'))
        media = (nota01 + nota02) / 2
        aluno_id = int(request.POST.get('aluno-id'))

        nota = Nota.objects.filter(aluno_id=aluno_id, materia_id=materia.id)

        for item in nota:
            item.nota_1 = nota01
            item.nota_2 = nota02
            item.media = media
            item.save()

        return redirect(f'/notas/{id}')

    lista_notas = []
    for aluno in alunos:
        nota = notas.filter(aluno_id=aluno.id)
        if nota:
            lista_notas.append({'nota01': nota[0].nota_1, 'nota02': nota[0].nota_2, 'media': nota[0].media})
        else:
            lista_notas.append({'nota01': 0.0, 'nota02': 0.0, 'media': 0.0})

    aluno_notas = zip(alunos, lista_notas)

    relacao = {'id': id, 'alunos': aluno_notas, 'materia': materia}
    return render(request, 'notas.html', {'relacao': relacao})


def nota_existe(aluno_id, materia):
    if aluno_id and materia:
        return Nota.objects.filter(aluno_id=aluno_id, materia_id=materia.id).exists()
    return False
