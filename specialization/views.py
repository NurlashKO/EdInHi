from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from specialization.models import Specialization


def all_specializations_view(request):
    all = Specialization.objects.all()
    return render(request, 'specialization/specializations.html', {'all': all})

def specialization_view(request, pk):
    specialization = get_object_or_404(Specialization, pk=pk)
    skills = specialization.skills.all()
    progress = 0
    if request.user.is_authenticated():
        passed_skills = request.user.skill_set.all()
        passed = 0
        for skill in skills:
            if skill in passed_skills:
                passed+=1
        progress = int(passed/specialization.skills.all().count() * 100)
    else:
            progress = 0
            passed_skills = None
    return render(request, 'specialization/specialization.html', {'passed_skills':passed_skills, 'specialization': specialization, 'progress': progress})
