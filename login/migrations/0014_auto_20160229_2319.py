# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_auto_20160220_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Onlinelist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('online', models.BooleanField(default=False)),
                ('user', models.ForeignKey(to='login.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
