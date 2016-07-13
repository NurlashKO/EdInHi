from django.db import models
from skill.models import Skill
from django.contrib.auth.models import User

class Specialization(models.Model):
	name = models.CharField(max_length=250, blank=True, default=None)
	description = models.TextField(max_length=250, blank=True)
	skills = models.ManyToManyField(Skill)
	users = models.ManyToManyField(User)
