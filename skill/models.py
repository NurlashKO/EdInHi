from django.db import models
from media.models import Book, Video

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    media_books = models.ManyToManyField(Book)
    media_video = models.ManyToManyField(Video)
