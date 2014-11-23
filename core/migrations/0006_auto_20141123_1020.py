# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20141123_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, max_length=75),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(unique=True, max_length=150),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='slug',
            field=models.SlugField(unique=True, max_length=150),
            preserve_default=True,
        ),
    ]
