from django.contrib import admin

from .models import Category, Restaurant, RestaurantLocation, Menu, MenuItem



class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'description',
    ]
    list_display = ['name']

class RestaurantLocationInline(admin.StackedInline):
    model = RestaurantLocation
    extra = 1

class RestaurantAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'plain_text_description',
        'markdown_description',
        'category',
        'managers',
        'phone',
    ]
    list_display = ['name', 'category', 'phone']
    inlines = [RestaurantLocationInline]

class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 3

class MenuAdmin(admin.ModelAdmin):
    fields = [
        'restaurant',
        'name',
        'plain_text_description',
        'markdown_description',
    ]
    list_display = ['name', 'plain_text_description']
    inlines = [MenuItemInline]




admin.site.register(Category, CategoryAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu, MenuAdmin)
