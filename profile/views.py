from django.shortcuts import render, redirect

def profile_view(request):
    if request.user.is_authenticated():
        if request.method == "POST":
            new_first_name = request.POST['firstName']
            new_last_name = request.POST['lastName']
            new_phone_number = request.POST['phoneNumber']

            newUser = request.user
            newUser.first_name = new_first_name
            newUser.last_name = new_last_name
            newUser.abstractuser.phone = new_phone_number
            newUser.save()
            newUser.abstractuser.save()

        else:
            return render(request, 'main_app/profile.html', {'user' : request.user})

        return redirect('index')
    else:
        return redirect('auth')