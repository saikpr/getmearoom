# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0026_auto_20141110_2026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='date_time_roll_1',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='date_time_roll_2',
        ),
    ]
