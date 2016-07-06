from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from main_app.models import AbstractUser
# Create your views here.

def all_users(request):
    all = User.objects.all()
    return render(request, 'users/users.html', {'users' : all})

def user_view(request, pk):
    user = get_object_or_404(User, pk = pk)
    return render(request, 'users/user.html', {'user' : user})
