# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miller', '0039_auto_20161111_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]