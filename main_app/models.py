from django.db import models
import datetime

# Create your models here.

'try to do one-to-one relation'
class TestUserProfile(models.Model):
    user_profile_university = models.CharField(max_length = 200)


class TestUser(models.Model):
    user_first_name = models.CharField(max_length = 200);
    user_last_name = models.CharField(max_length = 200);

    user_login_name = models.CharField(max_length = 200);
    'should be stored as MD-5 hash'
    user_password = models.CharField(max_length=50);

    user_email = models.CharField(max_length = 200);
    user_phone = models.CharField(max_length = 200);

    user_profile = models.ForeignKey(TestUserProfile, on_delete=models.CASCADE)



class TestProfession(models.Model):
    profession_name = models.CharField(max_length = 200);
    profession_field = models.CharField(max_length = 200);


class TestSkill(models.Model):
    skill_name = models.CharField(max_length = 200);
    skill_description = models.TextField(max_length = 500)



class TestTask(models.Model):
    task_name = models.CharField(max_length = 200);
    task_descriptino = models.TextField(max_length = 10000, default = "")
    task_id = models.IntegerField(default=0);
    pub_date = models.DateTimeField('date published', default = datetime.datetime.now())
