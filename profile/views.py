from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main_app.models import AbstractUser
from profile.forms import UploadFileForm
import os

def profile_view(request):
    if request.user.is_authenticated():
        if request.user.abstractuser.is_company == True:
            return redirect('/company')
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)

            new_first_name = request.POST['firstName']
            new_last_name = request.POST['lastName']
            new_organization = request.POST['organization']
            new_worked_at = request.POST['experience']
            new_phone_number = request.POST['phoneNumber']
            new_country = request.POST['country']
            new_city = request.POST['city']

            newUser = request.user
            newUser.first_name = new_first_name
            newUser.last_name = new_last_name
            newUser.abstractuser.organization = new_organization
            newUser.abstractuser.worked_at = new_worked_at
            newUser.abstractuser.phone = new_phone_number
            newUser.abstractuser.country = new_country
            newUser.abstractuser.city = new_city

            if form.is_valid():
                newUser.abstractuser.profile_image = request.FILES['file']

            newUser.save()
            newUser.abstractuser.save()

        else:
            return render(request, 'profile/profile.html', {'user' : request.user})

        return redirect('profile')
    else:
        return redirect('auth')

def profile_show(request, profile_id):
    profile = get_object_or_404(User, pk=profile_id)
    return render(request, 'profile/show.html', {'profile': profile})

@login_required
def passed_skills_view(request):
    skills = request.user.abstractuser.passed_skills.all()
    return render(request, 'profile/passedSkills.html', {'skills' : skills})
