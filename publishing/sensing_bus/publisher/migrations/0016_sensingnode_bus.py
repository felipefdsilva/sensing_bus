# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 17:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0015_remove_sensingnode_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensingnode',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='publisher.Bus', verbose_name='bus where the node is coupled'),
        ),
    ]
