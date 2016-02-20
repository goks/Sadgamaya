# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_user_tempfriendtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chattype',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
