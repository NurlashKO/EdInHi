from django.db import models
from skill.models import Skill
class Specialization(models.Model):
	name = models.CharField(max_length=250, blank=True, default=None)
	skills = models.ManyToManyField(Skill)
