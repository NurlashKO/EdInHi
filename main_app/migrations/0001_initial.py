# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-30 10:25
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('hide_contact_info', models.BooleanField(default=True)),
                ('send_email_about_new_work', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='pic_folder/')),
                ('data_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestProfession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession_name', models.CharField(max_length=200)),
                ('profession_field', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('task_descriptino', models.TextField(default='', max_length=10000)),
                ('task_id', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2016, 5, 30, 10, 25, 41, 545842, tzinfo=utc), verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_first_name', models.CharField(max_length=200)),
                ('user_last_name', models.CharField(max_length=200)),
                ('user_login_name', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=200)),
                ('user_phone', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TestUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_profile_university', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='testuser',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.TestUserProfile'),
        ),
        migrations.AddField(
            model_name='abstractuser',
            name='passed_skills',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.TestTask'),
        ),
        migrations.AddField(
            model_name='abstractuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
