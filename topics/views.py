from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from topics.models import Topic
from topics.forms import TopicForm

from django.db.models import Q


# Create your views here.

def index(request):
    # topic_list = Topic.objects.filter(name__contains="a") | Topic.objects.filter(description__icontains="b")
    # SELECT * FROM topics WHERE 

    topic_list = Topic.objects.filter(Q(name__contains="a") | Q(description__icontains="b"))

    context = {
        'topics': topic_list
    }
    return render(request, "topics/index.html", context)

def show(request,id):
    topic = Topic.objects.get(pk=id)
    context = {
        'topic': topic
    }
    return render(request, "topics/show.html", context)

def create(request):
    if request.method == "POST" and request.FILES['image_topic']:

        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            messages.success(request, "Topic cree avec succes")
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
        #     topic = Topic(name=topic_name, description=topic_description)
        #     topic.save()
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
    topic_to_update = Topic.objects.get(pk=id)
    form = TopicForm(instance=topic_to_update)

    if request.method == "POST" and request.FILES: 
        form = TopicForm(request.POST, request.FILES, instance=topic_to_update)
        if form.is_valid():
            form.save()
            messages.info(request, "Topic modifie avec succes")
            return redirect("topics-list")
        else:
            context = {
                "topic_form": form, 
                "topic_to_update": topic_to_update
            }
            return render(request, "topics/update.html", context)
        
    else:
        context = {
            "topic_form": form, 
            "topic_to_update": topic_to_update
        }
        return render(request, "topics/update.html", context)
        
        
        


def delete(request,id):
    topic = Topic.objects.get(pk=id)
    topic.is_deleted = True
    topic.save()
    messages.info(request, "Topic supprime avec succes")
    return redirect("topics-list")
