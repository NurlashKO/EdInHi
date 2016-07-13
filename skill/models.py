from django.db import models
from media.models import Book, Video

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    media_books = models.ManyToManyField(Book, blank=True)
    media_video = models.ManyToManyField(Video, blank=True)
    spec_logo = models.ImageField(upload_to='Images/skill_logo', blank=True, null=True)

    def __str__(self):
        return self.name
