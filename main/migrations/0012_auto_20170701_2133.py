# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-01 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170701_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='storeNum2',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
