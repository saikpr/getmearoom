# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_auto_20141029_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='warden',
            name='hostel_name',
            field=models.ForeignKey(to='portal.Hostel'),
        ),
    ]
