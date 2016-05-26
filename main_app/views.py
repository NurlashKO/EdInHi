from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    latest_task_list = TestTask.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main_app/index.html')
    return HttpResponse(template.render({'task_list': latest_task_list}, request))

