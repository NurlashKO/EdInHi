# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-13 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tasks', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='task',
            field=models.ManyToManyField(blank=True, to='tasks.CompanyTask'),
        ),
        migrations.AddField(
            model_name='vacancy',
            name='wishlist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.WishList'),
        ),
        migrations.AddField(
            model_name='company',
            name='QnA',
            field=models.ManyToManyField(to='company.QuestionAndAnswer'),
        ),
    ]
