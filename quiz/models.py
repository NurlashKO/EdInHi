from django.db import models
from main_app.models import AbstractUser
from skill.models import Skill


class Question(models.Model):
    question = models.CharField(max_length=250, blank=False)
    answer_right = models.CharField(max_length=250, blank=False)
    answer1 = models.CharField(max_length=250, blank=False)
    answer2 = models.CharField(max_length=250, blank=False)
    answer3 = models.CharField(max_length=250, blank=False)
    feedback = models.TextField(blank=True)
    # quizes = models.ManyToManyField(Quiz)

class Quiz(models.Model):
    title = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True)
    questions = models.ManyToManyField(Question, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

class SolvedQuestion(models.Model):
    question = models.ManyToManyField(Question)
    user = models.ManyToManyField(AbstractUser)

class SkillQuestion(models.Model):
    skill = models.ManyToManyField(Skill, blank=True)
    question = models.TextField(max_length=100, blank=True)
    answer = models.CharField(max_length=100, blank=True)
    answer1 = models.CharField(max_length=100, blank=True)
    answer2 = models.CharField(max_length=100, blank=True)
    answer3 = models.CharField(max_length=100, blank=True)
