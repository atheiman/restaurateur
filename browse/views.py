from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from core.models import Category, Restaurant, Tag, RestaurantLocation, Menu,\
  MenuItem, LocationReview, MenuItemReview



context_base = {
    'categories': Category.objects.all(),
}



# Show homepage
def index(request, zip=None):
    # TODO: filter restaurants locations by zip
    # TODO: order restaurants by rating
    restaurants = Restaurant.objects.all()[:15]

    context = context_base
    context['restaurants'] = restaurants

    return render(request, 'browse/index.html', context)



# Restaurant page
def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)

    # TODO: order restaurants by rating
    restaurants = Restaurant.objects.get_list_or_404(
        category=Category.objects.get(slug=category_slug)
    )[:15]

    context = context_base
    context['category'] = category
    context['restaurants'] = restaurants

    return render(request, 'browse/restaurant.html', context)



# Restaurant page
def restaurant(request, restaurant_slug):
    restaurant = Restaurant.objects.get_object_or_404(slug=restaurant_slug)

    context = context_base
    context['category'] = restaurant.category
    context['restaurant'] = restaurant

    return render(request, 'browse/restaurant.html', context)



def restaurant_location(request, restaurant_slug, location_id):
    restaurant = Restaurant.objects.get_object_or_404(slug=restaurant_slug)
    restaurant_location = RestaurantLocation.objects.get_object_or_404(pk=location_id)

    context = context_base
    context['category'] = restaurant.category
    context['restaurant'] = restaurant
    context['restaurant_location'] = restaurant_location

    return render(request, 'browse/restaurant_location.html', context)



def menu(request, restaurant_slug, menu_slug):
    restaurant = Restaurant.objects.get_object_or_404(slug=restaurant_slug)
    menu = Menu.objects.get_object_or_404(
        restaurant=Restaurant.objects.get(slug=restaurant_slug),
        slug=menu_slug
    )

    context = context_base
    context['category'] = restaurant.category
    context['restaurant'] = restaurant
    context['menu'] = menu

    return render(request, 'browse/menu.html', context)
