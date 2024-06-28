from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    return HttpResponse("Liste des tags")

def create(request):
    return HttpResponse("creation des tags")

def show(request,id):
    return HttpResponse(f"detail du tag ID {id}")

def update(request,id):
    return HttpResponse(f"modification du tag {id}")

def delete(request,id):
    return HttpResponse(f"suppression du tag {id}")
