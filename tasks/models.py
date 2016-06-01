from django.db import models
from django.contrib.postgres.fields import JSONField
import datetime


# Create your models here.
class Task(models.Model):
    task_id = models.IntegerField(default=0)
    task_requirements = JSONField()
    task_name = models.CharField(max_length = 200)
    task_description = models.TextField(max_length = 10000, default = "")
    task_problem = models.TextField(max_length = 10000, default = "")
    pub_date = models.DateTimeField('date published', default = datetime.datetime.now())

