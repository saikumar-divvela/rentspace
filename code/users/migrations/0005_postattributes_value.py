# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160517_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='postattributes',
            name='value',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]