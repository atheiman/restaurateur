# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20141123_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='plain_text_description',
            field=models.TextField(max_length=500, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurantlocation',
            name='plain_text_description',
            field=models.TextField(max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
