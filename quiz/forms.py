from django.forms import ModelForm
from .models import SkillQuestion
class QuestionForm(ModelForm):
    class Meta:
        model = SkillQuestion
