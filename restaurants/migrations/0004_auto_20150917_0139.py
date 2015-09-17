# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import restaurants.models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20150913_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='file',
            field=models.FileField(upload_to=b'menus/', validators=[restaurants.models.validate_file_extension]),
        ),
    ]
