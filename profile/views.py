from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from main_app.models import AbstractUser
from profile.forms import UploadFileForm


def profile_view(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                new_first_name = request.POST['firstName']
                new_last_name = request.POST['lastName']
                new_phone_number = request.POST['phoneNumber']

                newUser = request.user
                newUser.first_name = new_first_name
                newUser.last_name = new_last_name
                newUser.abstractuser.profile_image = request.FILES['file']
                newUser.abstractuser.phone = new_phone_number

                newUser.save()
                newUser.abstractuser.save()

        else:
            return render(request, 'profile/profile.html', {'user' : request.user})

        return redirect('index')
    else:
        return redirect('auth')