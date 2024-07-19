from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import login, logout, authenticate, get_user_model

# Create your views here.

User = get_user_model()

def register_view(request):

    if request.method == "POST": 
         # je recupere les donnees 

         firstname = request.POST.get("firstname")
         lastname = request.POST.get("lastname")
         email = request.POST.get("email")
         username = request.POST.get("username")
         password1 = request.POST.get("password1")
         password2 = request.POST.get("password2")

         # je verifie les password s'ils sont identiques

         if(password1 != password2):
             # si les passwords ne sont pas identique
            messages.error(request, "Les mots de passe ne sont pas identiques")
            return redirect("register")
         else:

            # si c'est identique  je creer le compte

            user = User.objects.create_user(
                username=username,
                password=password1,
                email=email
            ) 

            user.first_name = firstname
            user.last_name = lastname

            user.is_customer = True

            user.is_active = True
            user.save()

            if user is not None:
                # je le redirige vers la page de login
                messages.success(request, "Compte cree avec succes")
                return redirect("login")
            else:
                
            # sinon je renvoie un message d'erreur 
                messages.error(request, "Email ou mot de passe incorrect")
                return redirect("register")

            



    else: 
        return render(request, "core/register.html")

    # if request.method == "POST":
    #     firstname = request.POST.get("firstname")
    #     lastname = request.POST.get("lastname")
    #     email = request.POST.get("email")
    #     username = request.POST.get("username")
    #     password1 = request.POST.get("password1")
    #     password2 = request.POST.get("password2")

    #     if(password1 != password2):
    #         messages.error(request, "Les mots de passe ne sont pas identiques")
    #         return redirect("register")
    #     else:

    #         account = User.objects.create_user(
    #             username=username, 
    #             password=password1, 
    #             email=email, 
    #             first_name=firstname, 
    #             last_name=lastname
    #         )

    #         if account is not None:
    #             messages.success(request, "Compte cree avec succes")
    #             return redirect("login")
    #         else:
    #             messages.error(request, "Compte non cree")
    #             return redirect("register")
            
    # else:

    # return render(request, "core/register.html")



def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        print("------> username : ", username)
        print("------> password : ", password)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else: 
            messages.error(request, "Email ou mot de passe incorrect")
            return redirect("login")

    else:
        
        return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

def profile_view(request):

    context = {
        "current_user": request.user
    }

    return render(request, "core/profile.html", context)
