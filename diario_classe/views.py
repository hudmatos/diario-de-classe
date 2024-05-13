from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import redirect
from django.http.response import HttpResponse
from turmas.models import Relation_TPM
import pdb

def login(request):
    if request.method == "GET":
        return render(request, 'static/registration/login.html')
    else:
        current_username = request.POST.get('username')
        current_password = request.POST.get('password')

        user = authenticate(username=current_username, password=current_password)

        if user:
            auth.login(request, user)
            return redirect('/turmas/', {'user': user.id})
        else:
            return redirect("login")

