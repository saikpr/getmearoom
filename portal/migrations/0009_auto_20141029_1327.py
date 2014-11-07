# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0008_auto_20141029_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='department',
        ),
        migrations.RemoveField(
            model_name='batch',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='complaints',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Complaints',
        ),
        migrations.RemoveField(
            model_name='hostelalloted',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.RemoveField(
            model_name='hostelalloted',
            name='hostel_name',
        ),
        migrations.DeleteModel(
            name='HostelAlloted',
        ),
        migrations.DeleteModel(
            name='Notifications',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='hostel_name',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Preference',
        ),
        migrations.RemoveField(
            model_name='registration',
            name='roll_no',
        ),
        migrations.DeleteModel(
            name='Registration',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='warden',
            name='hostel_name',
        ),
        migrations.DeleteModel(
            name='Hostel',
        ),
        migrations.DeleteModel(
            name='Warden',
        ),
    ]
