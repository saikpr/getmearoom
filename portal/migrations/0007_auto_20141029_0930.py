# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20141029_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='warden',
            name='hostel_name',
            field=models.ForeignKey(default=b'Djanrajgiri', to='portal.Hostel'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='batch',
            name='department',
            field=models.ForeignKey(to='portal.Department'),
        ),
        migrations.AlterField(
            model_name='complaints',
            name='category',
            field=models.CharField(default=b'other', max_length=50),
        ),
        migrations.AlterField(
            model_name='hostelalloted',
            name='department',
            field=models.ForeignKey(to='portal.Department'),
        ),
        migrations.AlterField(
            model_name='hostelalloted',
            name='hostel_name',
            field=models.ForeignKey(to='portal.Hostel'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='hostel_name',
            field=models.ForeignKey(to='portal.Hostel'),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_alloted',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='warden',
            name='contact_no',
            field=models.CharField(max_length=10),
        ),
    ]
