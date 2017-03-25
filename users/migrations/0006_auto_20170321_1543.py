# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170321_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deliverable',
            field=models.FileField(blank=True, null=True, upload_to=users.models.get_path),
        ),
        migrations.AddField(
            model_name='task',
            name='users',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
