import json

from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from core.models import Category, Restaurant, Tag, RestaurantLocation, Menu,\
  MenuItem, LocationReview, MenuItemReview



context_base = {
    'categories': Category.objects.all(),
}



def index(request, zip=None):
    # TODO: filter restaurants locations by zip
    # TODO: order restaurants by rating
    restaurants = Restaurant.objects.all()[:15]

    context = context_base
    context['restaurants'] = restaurants

    return render(request, 'browse/index.html', context)



def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    # TODO: order restaurants by rating
    restaurants = Restaurant.objects.filter(
        category=Category.objects.get(slug=category_slug),
    )[:15]

    context = context_base
    context['category'] = category
    context['restaurants'] = restaurants

    return render(request, 'browse/category.html', context)



def restaurant(request, restaurant_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)

    context = context_base
    context['category'] = restaurant.category
    context['restaurant'] = restaurant

    return render(request, 'browse/restaurant.html', context)



def menu(request, restaurant_slug, menu_slug):
    restaurant = get_object_or_404(Restaurant, slug=restaurant_slug)
    menu = get_object_or_404(
        Menu,
        restaurant=restaurant,
        slug=menu_slug,
    )

    context = context_base
    context['category'] = restaurant.category
    context['restaurant'] = restaurant
    context['menu'] = menu

    return render(request, 'browse/menu.html', context)
