# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20170701_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='isOff',
            field=models.NullBooleanField(default=None),
        ),
    ]
