# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20160131_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='beacon',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
