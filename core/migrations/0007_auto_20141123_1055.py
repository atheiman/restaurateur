# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20141123_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='description',
            new_name='markdown_description',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='plain_text_description',
            field=models.TextField(default='default plain text description', max_length=500, blank=True),
            preserve_default=False,
        ),
    ]
