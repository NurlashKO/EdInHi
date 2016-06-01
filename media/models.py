from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=200)
    image = models.CharField(max_length=200, null=True, blank=True)

class Video(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=200)
