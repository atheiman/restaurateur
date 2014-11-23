from django.conf.urls import patterns, url

from .views import index, category, restaurant, restaurant_location, menu

urlpatterns = patterns('',
    # /
    url(
        r'^$',
        index,
        name='index',
    ),

    # /category_slug
    url(
        r'^(?P<category_slug>[a-z0-9_-]+)\/?$',
        category,
        name='category',
    ),

    # /restaurant_slug
    url(
        r'^(?P<restaurant_slug>[a-z0-9_-]+)\/?$',
        restaurant,
        name='restaurant',
    ),

    # /restaurant_slug/location_id
    url(
        r'^(?P<restaurant_slug>[a-z0-9_-]+)/(?P<location_id>[0-9]+)\/?$',
        restaurant_location,
        name='restaurant_location',
    ),

    # /restaurant_slug/menu_slug
    url(
        r'^(?P<restaurant_slug>[a-z0-9_-]+)/(?P<menu_slug>[a-z0-9_-]+)\/?$',
        menu,
        name='menu',
    ),
)
