# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-31 12:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20160121_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='beacon',
            field=models.TimeField(blank=True, default=datetime.datetime(2016, 1, 31, 12, 8, 25, 356986, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='signuptime',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 31, 12, 8, 36, 884237, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]