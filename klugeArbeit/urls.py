"""klugeArbeit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Kluge_arbeit.views import *

from django.contrib.auth.decorators import login_required

urlpatterns = [
    #url(r'^admin', admin.site.urls),
    #url(r'^', LoginView.as_view()),
    #url(r'^logout', LogoutView.as_view()),
    url(r'^$',logIn),
    url(r'^index$', index),
    url(r'^logout$', logOut),
    url(r'^enregistrement', signup),
    url(r'^chapitre$', getChapitre)
]
