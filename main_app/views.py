from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main_app/index.html')
    return HttpResponse(template.render({'task_list': latest_task_list}, request))

def task(request, task_id):
    task = get_object_or_404(TestTask, pk=task_id)
    return render(request, 'main_app/task.html', {'task': task})

def auth(request):
    template = loader.get_template('main_app/auth.html')
    return HttpResponse(template.render({}, request))

def reg(request):
    template = loader.get_template('main_app/reg.html')
    return HttpResponse(template.render({}, request))