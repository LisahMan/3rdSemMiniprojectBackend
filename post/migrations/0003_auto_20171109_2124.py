# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-09 15:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20171109_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 9, 21, 24, 28, 115974)),
        ),
    ]
