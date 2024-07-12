from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from tags.models import HashTag
from .forms import TagForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def index(request):

    tag_list = HashTag.objects.all()

    context = {
        'tags': tag_list
    }
    
    return render(request, "tags/index.html", context)

@login_required(login_url='login')
def create(request):
    if request.method == "POST":

        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tags-list")
        else:
            context = {
                "tag_form": form
            }
            return render(request, "tags/create.html", context)

    else:
        form = TagForm()
        context= {
            "tag_form": form
        }
        return render(request, "tags/create.html", context)

    return HttpResponse("creation des tags")

@login_required(login_url='login')
def show(request,id):
    tag = HashTag.objects.get(pk=id) # SELECT * FROM has-tags WHERE id = id

    

    context = {
        'tag': tag
    }
    return render(request, "tags/show.html", context)

@login_required(login_url='login')
def update(request,id):
    return HttpResponse(f"modification du tag {id}")

@login_required(login_url='login')
def delete(request,id):
    tag = HashTag.objects.get(pk=id)
    tag.delete()
    messages.info(request, "Tag supprime avec succes")
    return redirect("tags-list")
