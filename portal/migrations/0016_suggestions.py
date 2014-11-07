# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0015_auto_20141030_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'other', max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1000)),
                ('roll_no', models.ForeignKey(to='portal.Student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
