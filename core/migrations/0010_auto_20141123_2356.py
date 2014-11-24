# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20141123_1110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('plain_text_description', models.TextField(max_length=500, blank=True)),
                ('published', models.BooleanField(default=True, help_text=b'Display this special on the site?')),
                ('restaurant', models.ForeignKey(related_name='specials', to='core.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='markdown_description',
        ),
    ]
