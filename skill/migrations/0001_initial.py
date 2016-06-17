# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-15 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('media_books', models.ManyToManyField(to='media.Book')),
                ('media_video', models.ManyToManyField(to='media.Video')),
            ],
        ),
    ]
