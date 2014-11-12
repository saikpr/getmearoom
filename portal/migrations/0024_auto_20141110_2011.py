# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0023_auto_20141110_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roll_no_1',
            field=models.CharField(max_length=10),
        ),
    ]
