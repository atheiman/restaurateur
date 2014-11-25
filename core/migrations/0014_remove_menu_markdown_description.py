# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20141124_1535'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='markdown_description',
        ),
    ]
