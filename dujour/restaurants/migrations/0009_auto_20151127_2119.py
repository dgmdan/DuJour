# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20151105_2059'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItemTypeOption',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=9, null=True, decimal_places=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitemtype',
            name='price',
        ),
        migrations.AddField(
            model_name='menuitemtype',
            name='allow_many',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitemtype',
            name='is_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menuitemtypeoption',
            name='menu_item_type',
            field=models.ForeignKey(to='restaurants.MenuItemType', on_delete=models.CASCADE),
        ),
    ]
