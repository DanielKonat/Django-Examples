# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default='abc'),
        ),
        migrations.AlterField(
            model_name='student',
            name='rollno',
            field=models.TextField(),
        ),
    ]
