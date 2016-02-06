# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_user_chatactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friendslist',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
