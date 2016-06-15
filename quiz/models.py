from django.db import models

from main_app.models import AbstractUser
from skill.models import Skill

class Quiz(models.Model):
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)

    skills = models.ManyToManyField(Skill, blank=True)

class Question(models.Model):
    question = models.CharField(max_length=250, blank=False)
    answer_right = models.CharField(max_length=250, blank=False)
    answer1 = models.CharField(max_length=250, blank=False)
    answer2 = models.CharField(max_length=250, blank=False)
    answer3 = models.CharField(max_length=250, blank=False)
    feedback = models.TextField(blank=True)

    quizes = models.ManyToManyField(Quiz)

class SolvedQuestion(models.Model):
    question = models.ManyToManyField(Question)
    user = models.ManyToManyField(AbstractUser)
