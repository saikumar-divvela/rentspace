# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-07 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=50)),
                ('street', models.CharField(blank=True, max_length=20)),
                ('landmark', models.CharField(blank=True, max_length=25)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('pincode', models.CharField(blank=True, max_length=20)),
                ('google_map', models.CharField(blank=True, max_length=20)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=40)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('phone_number', models.CharField(blank=True, db_index=True, max_length=10, unique=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1)),
                ('date_of_birth', models.DateField(null=True)),
                ('id_card_type', models.CharField(blank=True, max_length=20)),
                ('idphoto', models.ImageField(blank=True, upload_to='')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login_date', models.DateTimeField(auto_now=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('is_email_verified', models.BooleanField(default=True)),
                ('is_phone_verified', models.BooleanField(default=True)),
                ('is_id_verified', models.BooleanField(default=True)),
                ('is_verified', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('id',),
                'db_table': 'user',
            },
        ),
    ]
