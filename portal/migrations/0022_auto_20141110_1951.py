# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0021_auto_20141110_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='f_floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='g_floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='s_floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hostelalloted',
            name='year',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='preference',
            name='pref1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='preference',
            name='pref2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registration',
            name='fee_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='registration',
            name='no_dues',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='registration',
            name='semester',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_alloted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='warden',
            name='warden_id',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
