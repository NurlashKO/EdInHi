from django.db import models
# Create your models here.
class Feedback(models.Model):
    sender_email = models.EmailField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
