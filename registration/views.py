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
    return render(request, "main_app/auth.html")


def reg_view(request):
    if (request.method == "POST"):
        print("Got in")
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=email).exists():
            return render(request, "main_app/reg.html")
        else:
            user = User.objects.create_user(email, email, password)
            user.save()
            user = authenticate(username=email, password=password)
            login(request, user)
            return redirect("index")
    else:
        return render(request, "main_app/reg.html")

def logout_view(request):
    logout(request)
    return redirect('index')
