# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 14:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20160616_1338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='zipcode',
            new_name='pincode',
        ),
    ]
