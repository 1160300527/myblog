# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.CharField(default='0000-00-00 00:00:00', max_length=32),
        ),
    ]