from django.contrib import admin
from .models import Company, QuestionAndAnswer, Vacancy
# Register your models here.
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(QuestionAndAnswer)
