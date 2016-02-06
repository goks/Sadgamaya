# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20160131_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chatactive',
            field=models.BooleanField(default=False),
        ),
    ]
