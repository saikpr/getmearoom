# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaints',
            name='compalint_id',
        ),
    ]
