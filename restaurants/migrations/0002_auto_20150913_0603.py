# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DayRestaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day_of_week', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='fax',
            field=models.CharField(default='', max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone',
            field=models.CharField(default='', max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dayrestaurant',
            name='restaurant',
            field=models.ForeignKey(to='restaurants.Restaurant'),
        ),
    ]
