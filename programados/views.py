from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from turmas.models import TPM
from . models import Programado
from datetime import date
import pdb

def programados(request, id):
    tpm = TPM(id)
    programados = Programado.objects.filter(turma_id=tpm['turma'].id, materia_id=tpm['materia'].id)
    

    if request.method == 'POST' and request.POST.get('id'):
        programado = Programado.objects.get(pk=request.POST.get('id'))
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if programado:
            programado.titulo = titulo
            programado.descricao = descricao
            programado.save()

        return redirect(f'/programados/{id}')

    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = date.today()

        programado = Programado(
            titulo = titulo,
            descricao = descricao,
            data = data,
            turma_id = tpm['turma'].id,
            materia_id = tpm['materia'].id
        )
        programado.save()

        return redirect(f'/programados/{id}')

    relacao = {'id': id, 'programados': programados, 'materia': tpm['materia']}
    return render(request, 'programados.html', {'relacao': relacao})

def edit(request, id):
    if id:
        programa = Programado.objects.get(pk=id)
        programa_dict = model_to_dict(programa)
        return JsonResponse({'programa': programa_dict})
    
def delete(request, id):
    relacao_id = request.GET.get('relacao')
    programado = Programado.objects.get(pk=id)
    if programado and relacao_id:
        programado.delete()
        return redirect(f'/programados/{relacao_id}')

