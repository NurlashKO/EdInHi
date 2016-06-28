from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from specialization.models import Specialization

def all_specializations_view(request):
    all = Specialization.objects.all()
    return render(request, 'specialization/specializations.html', {'all' : all})

def specialization_view(request, pk):
    specialization = get_object_or_404(Specialization, pk = pk)
    return render(request, 'specialization/specialization.html', {'specialization' : specialization})
