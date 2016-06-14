from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from company.models import Vacancy
from skill.models import Skill
from tasks.models import Task, CompanyTask

# Create your models here.

'try to do one-to-one relation'


class AbstractUser(models.Model):
    # Connect To Django authorization
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # IS COMPANY?
    is_company = models.BooleanField(default=False)

    # MAIN USER
    phone = models.CharField(max_length=20, null=True, blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True)
    hide_contact_info = models.BooleanField(default=True)
    send_email_about_new_work = models.BooleanField(default=True)
    profile_image = models.ImageField(upload_to='Images/', blank=True, null=True)
    data_of_birth = models.DateField(null=True, blank=True)
    passed_skills = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True, blank=True)

    # MAIN COMPANY
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='Images/', blank=True, null=True)
    web_page = models.CharField(max_length=100, null=True, blank=True)
    vacancies = models.ManyToManyField(Vacancy, blank=True)

    # Django authorization
    def create_profile(sender, **kwargs):
        user = kwargs["instance"]
        if kwargs["created"]:
            up = AbstractUser(user=user)
            up.save()

    post_save.connect(create_profile, sender=User)
