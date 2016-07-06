from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
            new_phone_number = request.POST['phoneNumber']

            newUser = request.user
            newUser.first_name = new_first_name
            newUser.last_name = new_last_name
            newUser.abstractuser.organization = new_organization
            newUser.abstractuser.phone = new_phone_number

            if form.is_valid():
                newUser.abstractuser.profile_image = request.FILES['file']

            newUser.save()
            newUser.abstractuser.save()

        else:
            return render(request, 'profile/profile.html', {'user' : request.user})

        return redirect('profile')
    else:
        return redirect('auth')
