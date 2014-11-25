# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_menu_markdown_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='plain_text_description',
            field=models.TextField(max_length=250, blank=True),
            preserve_default=True,
        ),
    ]
