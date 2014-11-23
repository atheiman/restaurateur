# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20141123_1002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='tag',
            new_name='tags',
        ),
    ]
