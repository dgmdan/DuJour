# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_auto_20151005_1354'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=6, max_digits=9)),
                ('menu', models.ForeignKey(to='restaurants.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemRegion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sw_lng', models.FloatField()),
                ('sw_lat', models.FloatField()),
                ('ne_lng', models.FloatField()),
                ('ne_lat', models.FloatField()),
                ('menu_item', models.ForeignKey(to='restaurants.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='MenuItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=6, max_digits=9)),
                ('menu_item', models.ForeignKey(to='restaurants.MenuItem')),
            ],
        ),
        migrations.AddField(
            model_name='menuitemregion',
            name='menu_item_type',
            field=models.ForeignKey(to='restaurants.MenuItemType', null=True),
        ),
    ]
