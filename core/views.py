from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomerForm

from django.contrib.auth import login, logout, authenticate, get_user_model

# Create your views here.
Account = get_user_model()

def home_view(request):

    context = {
        "form": CustomerForm()
    }

    return render(request, "core/home.html", context)

def about_view(request):
    return render(request, "core/about.html")


def contact_view(request):
    return render(request, "core/contact.html")

