# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-13 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_userpostbookings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpostbookings',
            name='post',
        ),
        migrations.RemoveField(
            model_name='userpostbookings',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserPostBookings',
        ),
    ]