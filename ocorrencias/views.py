from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Ocorrencia
from turmas.models import TPM 
from django.forms.models import model_to_dict
from datetime import date
import pdb

def ocorrencias(request, id):
    tpm = TPM(id)
    ocorrencias = Ocorrencia.objects.filter(turma_id=tpm['turma'].id, materia_id=tpm['materia'].id)

    if request.method == 'POST' and request.POST.get('id'):
        ocorrencia = Ocorrencia.objects.get(pk=request.POST.get('id'))
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')

        if ocorrencia:
            ocorrencia.titulo = titulo
            ocorrencia.descricao = descricao
            ocorrencia.save()

        return redirect(f'/ocorrencias/{id}/')

    elif request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = date.today()

        ocorrencia = Ocorrencia(
            titulo = titulo,
            descricao = descricao,
            data = data,
            turma_id = tpm['turma'].id,
            materia_id = tpm['materia'].id
        )
        ocorrencia.save()

        return redirect(f'/ocorrencias/{id}/')

    relacao = {'id': id, 'ocorrencias': ocorrencias, 'materia': tpm['materia']}
    return render(request, 'ocorrencia.html', {'relacao': relacao})

def edit(request, id):
    if id:
        ocorrencia = Ocorrencia.objects.get(pk=id)
        ocorrencia_dict = model_to_dict(ocorrencia)
        return JsonResponse({'ocorrencia': ocorrencia_dict})
    
def delete(request, id):
    relacao_id = request.GET.get('relacao')
    ocorrencia = Ocorrencia.objects.get(pk=id)
    if ocorrencia and relacao_id:
        ocorrencia.delete()
        return redirect(f'/ocorrencias/{relacao_id}')

