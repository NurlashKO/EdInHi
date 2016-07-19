# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-19 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quizes',
        ),
        migrations.AddField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(blank=True, to='quiz.Question'),
        ),
    ]
