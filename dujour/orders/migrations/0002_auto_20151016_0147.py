# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(null=True, to='restaurants.MenuItem', on_delete=models.CASCADE),
        ),
    ]
