from django.shortcuts import render, get_object_or_404
from .models import CompanyTask

# Create your views here.

def company_task(request, task_id):
    task = get_object_or_404(CompanyTask, pk=task_id)
    return render(request, 'ctask/company_task.html', {'task':task})
