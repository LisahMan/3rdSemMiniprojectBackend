# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-09 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_information', '0002_userinformation_follow_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='follow_field',
            field=models.CharField(max_length=2),
        ),
    ]
