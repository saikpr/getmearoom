# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0020_auto_20141110_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_no',
            field=models.IntegerField(),
        ),
    ]
