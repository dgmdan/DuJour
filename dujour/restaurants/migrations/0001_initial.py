# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20, null=True, blank=True)),
                ('fax', models.CharField(max_length=20, null=True, blank=True)),
                ('website', models.CharField(max_length=255)),
            ],
        ),
    ]
