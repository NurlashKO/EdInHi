from django.db import models
from skill.models import Skill


# Create your models here.

class QuestionAndAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()


class Company(models.Model):
    QnA = models.ManyToManyField(QuestionAndAnswer)


class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100)
    required_skills = models.ManyToManyField(Skill, blank=True)
