# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lunchpac', '0002_auto_20150921_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
