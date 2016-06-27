from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from specialization.models import Specialization

def all_specializations(request):
    all = Specialization.objects.all()

    return render(request, 'specializations.html', {'all' : all})