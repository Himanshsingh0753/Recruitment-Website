# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-10 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0005_auto_20160710_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditrecdata',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
