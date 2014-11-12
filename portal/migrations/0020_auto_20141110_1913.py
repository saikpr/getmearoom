# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20141110_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='hostel_name',
            field=models.ForeignKey(to='portal.Hostel'),
        ),
        migrations.AlterField(
            model_name='room',
            name='roll_no_1',
            field=models.ForeignKey(to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='room',
            name='roll_no_2',
            field=models.CharField(max_length=10),
        ),
    ]
