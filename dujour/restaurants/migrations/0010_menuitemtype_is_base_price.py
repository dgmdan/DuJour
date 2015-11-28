# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20151127_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitemtype',
            name='is_base_price',
            field=models.BooleanField(default=False),
        ),
    ]
