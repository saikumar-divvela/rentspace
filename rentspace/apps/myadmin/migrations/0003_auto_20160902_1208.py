# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0002_auto_20160902_1202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postbox',
            old_name='phone',
            new_name='phone_number',
        ),
    ]
