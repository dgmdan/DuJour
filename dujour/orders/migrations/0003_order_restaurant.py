# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20151105_2059'),
        ('orders', '0002_auto_20151016_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(default=1, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
    ]
