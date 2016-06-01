from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    name='main_app/base.html'
    if request.user.is_authenticated():
        name='main_app/loginBase.html'
        #pnum = request.user.abstractuser.phone
    return render(request, 'main_app/index.html', {'template': name})

def task(request, task_id):
    task = get_object_or_404(TestTask, pk=task_id)
    return render(request, 'main_app/task.html', {'task':task})
