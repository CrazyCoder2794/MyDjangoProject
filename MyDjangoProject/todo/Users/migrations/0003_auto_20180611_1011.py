# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-06-11 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20180529_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
