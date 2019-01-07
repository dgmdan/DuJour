# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20150913_0603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'menus/')),
                ('restaurant', models.ForeignKey(to='restaurants.Restaurant', on_delete=models.CASCADE)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dayrestaurant',
            options={'verbose_name': 'Assigned day of week', 'verbose_name_plural': 'Assigned days of week'},
        ),
        migrations.AlterField(
            model_name='dayrestaurant',
            name='day_of_week',
            field=models.IntegerField(choices=[(0, b'Sunday'), (1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday')]),
        ),
    ]
