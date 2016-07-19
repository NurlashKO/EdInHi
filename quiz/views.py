from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Quiz, Question, SolvedQuestion

@login_required
def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    quiz_questions = quiz.questions.all()

    user_answered_questions = request.user.abstractuser.solvedquestion_set.all()
    user_answeredArray = []
    for somee in user_answered_questions:
        for t in somee.question.all():
            user_answeredArray.append(t)

    completed = True
    for t in quiz_questions:
        if t not in user_answeredArray:
            completed = False

    if request.method == "POST":

        userAns = request.POST.getlist('checks[]')
        print(userAns)

        rightAns = []
        for quest in quiz.questions.all():
            rightAns.append(quest.answer_right)

        if userAns == rightAns:
            for quest in quiz.questions.all():
                a = SolvedQuestion()
                a.save()

                a.question.add(quest)
                a.user.add(request.user.abstractuser)
            return redirect("index")

    return render(request, 'quiz/quiz.html', {'quiz' : quiz,
                                         'completed' : completed})

def skill_quiz_view(request, skill_id):
    skill = get_object_or_404(Skill, pk=skill_id)
    skill_questions = skill.questions_set.all()
    return render(request, 'quiz/skill_quiz.html', {'skill_questions':skill_questions, 'skill':skill})
