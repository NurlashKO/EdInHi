from django.db import models
from django.contrib.auth.models import User
from skill.models import Skill
from tasks.models import CompanyTask

# Create your models here.

class QuestionAndAnswer(models.Model):
    question = models.TextField()
    answer = models.TextField()

class Company(models.Model):
    QnA = models.ManyToManyField(QuestionAndAnswer)

class WishList(models.Model):
    user = models.OneToOneField(User)

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.CharField(max_length=100)
    required_skills = models.ManyToManyField(Skill, blank=True)
    task = models.ManyToManyField(CompanyTask, blank=True)
    wishlist = models.ForeignKey(WishList)



