# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from form import *


def getChapitre(request):
    chap = ["python", "c++", "pascal", "java"]

    return render(request, "Kluge_arbeit/backoffice/chapitre.html", locals())

def index(request):
    return render(request, "Kluge_arbeit/index.html")

def logIn(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return render(request, "Kluge_arbeit/index.html", locals())
            else:  # sinon une erreur sera affichée
                error = True

    else:
        form = ConnexionForm()

    return render(request, "Kluge_arbeit/login.html", locals())

def logOut(request):
    logout(request)
    return redirect(reverse(logIn))

def signup(request):
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse(logIn))
    else:
        form = Registerform()
    return render(request, 'Kluge_arbeit/singup.html', locals())
