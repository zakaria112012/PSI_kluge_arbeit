# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from form import *


def getChapitre(request):
    chap = ["python", "c++", "pascal", "java"]

    return render(request, "Kluge_arbeit/backoffice/chapitre.html", locals())

def index(request):
    return render(request, "Kluge_arbeit/index.html")

def logIn(request):


    return render(request, "Kluge_arbeit/login.html", locals())

def logOut(request):
    return render(request, "Kluge_arbeit/index.html")

def signup(request):

    return render(request, 'Kluge_arbeit/singup.html', locals())
