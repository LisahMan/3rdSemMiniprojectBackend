# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-08 18:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 0, 13, 18, 905955)),
        ),
    ]