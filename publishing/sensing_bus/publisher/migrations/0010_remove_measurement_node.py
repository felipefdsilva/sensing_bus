# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0009_auto_20170407_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='node',
        ),
    ]
