from django.db import models
from skill.models import Skill
from tasks.models import Task
# Create your models here.
class Specialization(models.Model):
	skills = models.ForeignKey(Skill)
	tasks = models.ForeignKey(Task)
	"""docstring for Specialization"""
