# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0002_skill_id_in_spec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='id_in_spec',
            field=models.IntegerField(blank=True),
        ),
    ]
