# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-17 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='facilities',
            field=models.CharField(blank=True, max_length=512),
        ),
    ]
