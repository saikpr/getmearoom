# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0017_auto_20141106_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_no', models.IntegerField(max_length=1)),
                ('hostel_name', models.ForeignKey(to='portal.Hostel')),
                ('roll_no_1', models.ForeignKey(related_name=b'roll1', to='portal.Student')),
                ('roll_no_2', models.ForeignKey(related_name=b'roll2', to='portal.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
