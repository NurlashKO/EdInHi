from django.db import models
from media.models import Book, Video
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    media_books = models.ManyToManyField(Book, blank=True)
    media_video = models.ManyToManyField(Video, blank=True)
    spec_logo = models.ImageField(upload_to='Images/skill_logo', blank=True, null=True)
    short_description = models.TextField(max_length=250, null=True, blank="")

    solved_users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name
