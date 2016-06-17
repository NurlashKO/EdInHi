from django import forms
from .models import Vacancy, CompanyTask
from main_app.models import AbstractUser

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ("name", "description", "salary")

class TaskForm(forms.ModelForm):
    class Meta:
        model = CompanyTask
        fields = ('name', 'comment_to_task', 'description', 'contact_email', 'phone')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = AbstractUser
        fields = ('name', 'description', 'web_page', 'email', 'contact_phone', 'logo')
