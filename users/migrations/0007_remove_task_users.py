# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170321_1543'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='users',
        ),
    ]