from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from guestbook import models

def index(request):
    return render(request, 'guestbook/index.html')

def add(request):
    name = request.POST["name"]
    password = request.POST["password"]
    content = request.POST["content"]

    models.add(name, password, content)
    return HttpResponseRedirect('/guestbook/add')