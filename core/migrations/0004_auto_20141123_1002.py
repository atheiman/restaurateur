# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20141121_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationreview',
            name='location',
            field=models.ForeignKey(related_name='location_reviews', to='core.RestaurantLocation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitemreview',
            name='menu_item',
            field=models.ForeignKey(related_name='menu_item_reviews', to='core.MenuItem'),
            preserve_default=True,
        ),
    ]
