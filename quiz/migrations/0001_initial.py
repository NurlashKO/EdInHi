# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-13 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
        ('skill', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer_right', models.CharField(max_length=250)),
                ('answer1', models.CharField(max_length=250)),
                ('answer2', models.CharField(max_length=250)),
                ('answer3', models.CharField(max_length=250)),
                ('feedback', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('skills', models.ManyToManyField(blank=True, to='skill.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='SolvedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ManyToManyField(to='quiz.Question')),
                ('user', models.ManyToManyField(to='main_app.AbstractUser')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quizes',
            field=models.ManyToManyField(to='quiz.Quiz'),
        ),
    ]
