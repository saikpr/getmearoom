# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0018_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hostel_name',
            field=models.ForeignKey(related_name=b'hostel', to='portal.Hostel'),
        ),
    ]
