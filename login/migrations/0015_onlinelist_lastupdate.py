# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0014_auto_20160229_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinelist',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
