# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-05-29 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=10)),
                ('deadline', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='todo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Users'),
        ),
    ]
