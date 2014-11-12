# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_auto_20141110_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='fee_id',
            field=models.CharField(max_length=15),
        ),
    ]
