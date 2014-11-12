# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0024_auto_20141110_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_no', models.IntegerField()),
                ('roll_no_1', models.CharField(max_length=10)),
                ('roll_no_2', models.CharField(max_length=10)),
                ('hostel_name', models.ForeignKey(to='portal.Hostel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='room',
            name='hostel_name',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
