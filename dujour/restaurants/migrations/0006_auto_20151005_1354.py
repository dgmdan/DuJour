# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import dujour.restaurants.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0005_auto_20150918_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='file',
            field=models.ImageField(upload_to='static/menus/', validators=[dujour.restaurants.models.validate_file_extension]),
        ),
    ]
