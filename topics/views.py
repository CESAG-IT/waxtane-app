from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from topics.models import Topic
from topics.forms import TopicForm


# Create your views here.

def index(request):
    topic_list = Topic.objects.all()

    context = {
        'topics': topic_list
    }
    return render(request, "topics/index.html", context)

def show(request,id):
    return render(request, "topics/show.html")

def create(request):
    if request.method == "POST":

        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("topics-list")
        else:
            context = {
                "topic_form": form
            }
            return render(request, "topics/create.html", context)
        # topic_name = request.POST.get("name")
        # topic_description = request.POST.get("description")

        # try:
        #     Topic.objects.create(name=topic_name, description=topic_description)
        #     return redirect("topics-list")

        # except Exception as e:
        #     messages.error(request, e)
        #     return redirect("topics-create")
    else:
        form = TopicForm()
        context= {
            "topic_form": form
        }
        return render(request, "topics/create.html", context)

def update(request,id):
    return render(request, "topics/update.html")

def delete(request,id):
    topic = Topic.objects.get(pk=id)
    topic.delete()
    return redirect("topics-list")
