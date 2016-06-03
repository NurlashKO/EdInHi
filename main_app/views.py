from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    name='main_app/base.html'
    return render(request, 'main_app/index.html', {'template': name})

#What task is it?
def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'main_app/task.html', {'task':task})
