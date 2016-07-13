from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from specialization.models import Specialization

def all_specializations_view(request):
    all = Specialization.objects.all()
    return render(request, 'specialization/specializations.html', {'all' : all})

def specialization_view(request, pk):
    specialization = get_object_or_404(Specialization, pk = pk)
    skills = specialization.skills.all()
    passed_skills = request.user.AbstractUser.passed_skills.all()
    passed = 0
    for skill in skills:
        for passed_skill in passed_skills:
            if passed_skill == skill
                passed++
    progress = passed/skills.all.count()
    return render(request, 'specialization/specialization.html', {'specialization' : specialization, 'progress' : progress})
