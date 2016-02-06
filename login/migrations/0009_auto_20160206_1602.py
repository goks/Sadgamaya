# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20160206_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default=login.models.generatetoken, unique=True, max_length=16, editable=False),
        ),
    ]
