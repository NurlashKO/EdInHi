from django.db import models
from media.models import Book, Video

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    media_books = models.ManyToManyField(Book, blank=True)
    media_video = models.ManyToManyField(Video, blank=True)
    id_in_spec = models.IntegerField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.id_in_spec = self.specialization.skill_set.all().count()+1
        super(Skill, self).save(*args, **kwargs)
