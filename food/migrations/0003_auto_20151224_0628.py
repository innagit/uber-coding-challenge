# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 06:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20151224_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='dayhour',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AlterField(
            model_name='truck',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 23, 6, 28, 54, 143877)),
        ),
        migrations.AlterField(
            model_name='truck',
            name='food_item',
            field=models.CharField(default=None, max_length=500),
        ),
    ]