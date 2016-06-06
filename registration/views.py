import re

from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib import messages
# Create your views here.


def auth_view(request):
    if (request.method == "POST"):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "registration/auth.html")


def reg_view(request):
    if (request.method == "POST"):
        print("Got in")
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$', password) and password==repassword:
            if User.objects.filter(username=email).exists():
                return render(request, "registration/reg.html")
            else:
                user = User.objects.create_user(username=email, email=email, password=password)
                user.save()
                user = authenticate(username=email, password=password)
                login(request, user)
                return render(request, "profile/profile.html")
        else:
            return render(request, "registration/reg.html")
    else:
        return render(request, "registration/reg.html")

def logout_view(request):
    logout(request)
    return redirect('index')
