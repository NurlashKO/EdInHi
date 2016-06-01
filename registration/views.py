from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
import re

# Create your views here.

#Authorization : Login
def auth_view(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, "main_app/auth.html")

#Authorization : Registration
def reg_view(request):

    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']

        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', password):

            if User.objects.filter(username=email).exists():
                return render(request, "main_app/reg.html")

            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                user = authenticate(username=email, password=password)
                login(request, user)
                return redirect("index")

        else:
            return render(request, "main_app/reg.html")

    else:
        return render(request, "main_app/reg.html")

def logout_view(request):
    logout(request)
    return redirect("index")

