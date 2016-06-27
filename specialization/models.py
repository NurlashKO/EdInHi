from django.db import models

class Specialization(models.Model):
	name = models.CharField(max_length=250, blank=True, default=None)