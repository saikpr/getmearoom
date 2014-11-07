# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_complaints_compalint_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notifiactions',
            new_name='Notifications',
        ),
    ]
