from django.shortcuts import render, get_object_or_404
from .models import Skill
from random import shuffle

# Create your views here.
def skill(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    # print(skill.name)
    # print(skill.skillquestion_set.count())
    skill_questions = skill.skillquestion_set.all()
    for q in skill_questions:
        answers = [q.answer, q.answer1, q.answer2, q.answer3]
        shuffle(answers)
        q.answer, q.answer1, q.answer2, q.answer3 = answers
    # for question in skill_questions:
    #     print(question.answer)
    return render(request, 'skill/skill.html', {'skill':skill, 'skill_questions':skill_questions})
