# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20160206_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tempfriendtoken',
            field=models.CharField(default=b'0', max_length=254, null=True),
        ),
    ]
