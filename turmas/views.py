from django.shortcuts import render
from . models import Relation_TPM, Turma, Professor, Materia
from django.urls import reverse
import pdb

def turmas(request):
    current_user = request.user
    # TPM (TURMA, PROFESSOR, MATERIA)
    tpm = Relation_TPM.objects.filter(professor_id=current_user.id)
    
   
    relacao = []
    for item in tpm:
        turma = Turma.objects.get(pk=item.turma_id)
        professor = Professor.objects.get(pk=item.professor_id)
        materia = Materia.objects.get(pk=item.materia_id)
       
        relacao.append({'id': item.id, 'turma': turma, 'professor': professor, 'materia': materia})

    return render(request, 'turmas.html', {'relacao': relacao})

def home(request, id):
    tpm = Relation_TPM.objects.get(pk=id)

    turma = Turma.objects.get(pk=tpm.turma_id)
    professor = Professor.objects.get(pk=tpm.professor_id)
    materia = Materia.objects.get(pk=tpm.materia_id)

    relacao = {'id': id, 'turma': turma, 'professor': professor, 'materia': materia}

    return render(request, 'home.html', {'relacao': relacao})
