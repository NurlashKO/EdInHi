from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

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

