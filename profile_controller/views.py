from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def profile_view(request):
    if request.user.is_authenticated():
        print ("sfsfsfdffsfs")
        return render(request, 'profile_controller/profileHTML.html')
    else:
        return redirect('auth')