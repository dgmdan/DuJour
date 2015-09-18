# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import restaurants.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20150917_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dayrestaurant',
            name='day_of_week',
            field=models.IntegerField(choices=[(0, 'Sunday'), (1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday')]),
        ),
        migrations.AlterField(
            model_name='menu',
            name='file',
            field=models.FileField(upload_to='menus/', validators=[restaurants.models.validate_file_extension]),
        ),
    ]
