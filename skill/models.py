from django.db import models
from media.models import Book, Video

from specialization.models import Specialization

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    media_books = models.ManyToManyField(Book)
    media_video = models.ManyToManyField(Video)
    specialization = models.ForeignKey(Specialization, blank=True)
