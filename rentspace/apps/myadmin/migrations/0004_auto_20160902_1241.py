# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-02 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myadmin', '0003_auto_20160902_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postbox',
            old_name='created_date',
            new_name='sent_date',
        ),
    ]
