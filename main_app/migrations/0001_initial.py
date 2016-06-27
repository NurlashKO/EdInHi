# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 05:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbstractUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_company', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('organization', models.CharField(blank=True, max_length=100, null=True)),
                ('hide_contact_info', models.BooleanField(default=True)),
                ('send_email_about_new_work', models.BooleanField(default=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('data_of_birth', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='Images/')),
                ('web_page', models.CharField(blank=True, max_length=100, null=True)),
                ('passed_skills', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='skill.Skill')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancies', models.ManyToManyField(blank=True, to='company.Vacancy')),
            ],
        ),
    ]
