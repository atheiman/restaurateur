# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20141123_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='description',
            new_name='plain_text_description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='description',
        ),
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='plain_text_description',
            field=models.CharField(default='default plain text description', max_length=250, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='markdown_description',
            field=models.TextField(default='default plain text description', help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='plain_text_description',
            field=models.TextField(default='default plain text description', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='markdown_description',
            field=models.TextField(default='default markdown description', help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=500, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurantlocation',
            name='plain_text_description',
            field=models.TextField(default='default plain text description', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='plain_text_description',
            field=models.TextField(max_length=500),
            preserve_default=True,
        ),
    ]
