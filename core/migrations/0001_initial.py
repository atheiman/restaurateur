# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=75)),
                ('description', models.CharField(help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=250, blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('slug', models.SlugField(max_length=75)),
                ('description', models.TextField(help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=250, blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75)),
                ('description', models.TextField(max_length=150, blank=True)),
                ('spicy', models.BooleanField(default=False)),
                ('featured', models.BooleanField(default=False)),
                ('allergies', models.CharField(max_length=75, blank=True)),
                ('menu', models.ForeignKey(related_name='items', to='core.Menu')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField(help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=500, blank=True)),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('category', models.ForeignKey(related_name='restaurants', to='core.Category')),
                ('managers', models.ManyToManyField(related_name='restaurants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RestaurantLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(help_text=b"This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>.", max_length=250, blank=True)),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(11111)])),
                ('phone', models.CharField(max_length=10, blank=True)),
                ('restaurant', models.ForeignKey(related_name='locations', to='core.Restaurant')),
            ],
            options={
                'ordering': ['city'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now=True)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('comment', models.TextField(max_length=250, blank=True)),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItemReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Review')),
                ('menu_item', models.ForeignKey(related_name='reviews', to='core.MenuItem')),
            ],
            options={
            },
            bases=('core.review',),
        ),
        migrations.CreateModel(
            name='LocationReview',
            fields=[
                ('review_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Review')),
                ('location', models.ForeignKey(related_name='reviews', to='core.RestaurantLocation')),
            ],
            options={
            },
            bases=('core.review',),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=75)),
            ],
            options={
                'ordering': ['slug'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tag',
            field=models.ManyToManyField(to='core.Tag', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(related_name='menus', to='core.Restaurant'),
            preserve_default=True,
        ),
    ]
