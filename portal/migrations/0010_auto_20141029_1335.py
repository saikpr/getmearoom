# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_auto_20141029_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(default=b'other', max_length=50)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('hostel_name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('g_floor', models.IntegerField(default=0, max_length=3)),
                ('f_floor', models.IntegerField(default=0, max_length=3)),
                ('s_floor', models.IntegerField(default=0, max_length=3)),
                ('image_path', models.CharField(max_length=200)),
                ('rating', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HostelAlloted',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=1)),
                ('department', models.ForeignKey(to='portal.Department')),
                ('hostel_name', models.ForeignKey(to='portal.Hostel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roll_no_sender', models.CharField(max_length=10)),
                ('roll_no_reciever', models.CharField(max_length=10)),
                ('status', models.IntegerField(default=0, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pref1', models.IntegerField(max_length=3)),
                ('pref2', models.IntegerField(max_length=3)),
                ('hostel_name', models.ForeignKey(to='portal.Hostel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=1)),
                ('semester', models.IntegerField(max_length=2)),
                ('no_dues', models.IntegerField(default=0, max_length=1)),
                ('fee_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('roll_no', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('contact_no', models.CharField(max_length=10)),
                ('room_alloted', models.IntegerField(default=0, max_length=3)),
                ('father_name', models.CharField(max_length=40)),
                ('mother_name', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=400)),
                ('gender', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Warden',
            fields=[
                ('warden_id', models.IntegerField(max_length=10, serialize=False, primary_key=True)),
                ('warden_name', models.CharField(max_length=40)),
                ('contact_no', models.CharField(max_length=10)),
                ('hostel_name', models.ForeignKey(to='portal.Hostel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='registration',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='preference',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='complaints',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batch',
            name='department',
            field=models.ForeignKey(to='portal.Department'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batch',
            name='roll_no',
            field=models.ForeignKey(to='portal.Student', unique=True),
            preserve_default=True,
        ),
    ]
