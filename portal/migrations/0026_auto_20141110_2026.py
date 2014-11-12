# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0025_auto_20141110_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='date_time_roll_1',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 10, 20, 26, 5, 92500), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rooms',
            name='date_time_roll_2',
            field=models.DateTimeField(default=datetime.date(2014, 11, 10), auto_now_add=True),
            preserve_default=False,
        ),
    ]
