# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-13 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialization', '0002_specialization_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
