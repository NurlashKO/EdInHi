from django import forms
from .models import Vacancy, CompanyTask

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("name", "description", "salary")

class TaskForm(forms.ModelForm):
    class Meta:
        model = CompanyTask
        fields = ('name', 'comment_to_task', 'description', 'contact_email', 'phone')
