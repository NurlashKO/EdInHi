from django.db import models
from skill.models import Skill
from django.utils import timezone

from specialization.models import Specialization

class Task(models.Model):
    name = models.CharField(max_length = 200)
    description = models.TextField(max_length = 10000, default = "")
    problem = models.TextField(max_length = 10000, default = "")
    pub_date = models.DateTimeField('date published', default = timezone.now)
    specialization = models.ForeignKey(Specialization, blank=True)
    id_in_spec = models.IntegerField(blank=True)

    def save(self, *args, **kwargs):
        self.id_in_spec = self.specialization.task_set.all().count()+1
        super(Task, self).save(*args, **kwargs)

class CompanyTask(models.Model):
    name = models.CharField(max_length=200)
    comment_to_task = models.TextField()
    description = models.TextField()
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    pub_date = models.DateTimeField('date published', default = timezone.now)
