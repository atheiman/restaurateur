# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_restaurantlocation_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantlocation',
            options={'ordering': ['name']},
        ),
    ]
