# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_batch_complaints_hostel_hostelalloted_notifiactions_preference_registration_student_warden'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_name', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('hod_name', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
