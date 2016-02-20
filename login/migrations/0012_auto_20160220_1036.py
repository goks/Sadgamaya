# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_user_chattype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signuptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
