# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-25 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay', '0003_auto_20181025_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='password',
        ),
        migrations.AddField(
            model_name='account',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
