# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-16 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digispaceapp', '0002_auto_20160715_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='speciality',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
