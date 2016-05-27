from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
    if(request.method == "POST"):
        print("Got in")
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(email, email, password)
        user.save()
        user = authenticate(username=email, password=password)
        login(request, user)
        return redirect("index")
    else:
        return render(request, "main_app/reg.html")

