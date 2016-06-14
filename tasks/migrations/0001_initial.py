# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-13 13:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField(default=0)),
                ('task_name', models.CharField(max_length=200)),
                ('task_description', models.TextField(default='', max_length=10000)),
                ('task_problem', models.TextField(default='', max_length=10000)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2016, 6, 13, 19, 41, 30, 869453), verbose_name='date published')),
            ],
        ),
    ]
