# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20160220_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signuptime',
            field=models.DateTimeField(),
        ),
    ]
