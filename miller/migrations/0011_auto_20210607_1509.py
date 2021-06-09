# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-06-07 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0010_auto_20210604_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='latitude',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='longitude',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='mapid',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='story',
            name='maptype',
            field=models.CharField(default=b'opengreenmap', max_length=50),
        ),
    ]
