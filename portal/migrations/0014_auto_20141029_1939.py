# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0013_verification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verification',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
        ),
    ]
