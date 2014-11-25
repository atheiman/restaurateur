# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20141124_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2, validators=[django.core.validators.MinValueValidator(10)]),
            preserve_default=True,
        ),
    ]
