# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-04 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20170704_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='truck',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
