# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_onlinelist_lastupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinelist',
            name='user',
            field=models.ForeignKey(to='login.User', unique=True),
        ),
    ]
