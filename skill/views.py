from django.shortcuts import render, get_object_or_404
from .models import Skill

# Create your views here.
def skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    return render(request, 'skill/skill.html', {'skill':skill})
