# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20141028_0646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='status',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
