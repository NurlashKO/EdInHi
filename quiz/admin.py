from django.contrib import admin
from .models import Question, Quiz, SolvedQuestion, SkillQuestion

# Register your models here.

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(SolvedQuestion)
admin.site.register(SkillQuestion)
