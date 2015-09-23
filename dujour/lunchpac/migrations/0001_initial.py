# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('order_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('restaurant_id', models.IntegerField()),
                ('add_date', models.DateTimeField()),
                ('order_item', models.CharField(max_length=100)),
                ('comments', models.TextField()),
            ],
        ),
    ]
