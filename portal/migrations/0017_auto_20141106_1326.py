# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0016_suggestions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='roll_no',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
