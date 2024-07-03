from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from tags.models import HashTag

# Create your views here.

def index(request):

    tag_list = HashTag.objects.all()

    context = {
        'tags': tag_list
    }
    
    return render(request, "tags/index.html", context)

def create(request):
    return HttpResponse("creation des tags")

def show(request,id):
    tag = HashTag.objects.get(pk=id) # SELECT * FROM has-tags WHERE id = id

    context = {
        'tag': tag
    }
    return render(request, "tags/show.html", context)

def update(request,id):
    return HttpResponse(f"modification du tag {id}")

def delete(request,id):
    return HttpResponse(f"suppression du tag {id}")
