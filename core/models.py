from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.CharField(max_length=250, blank=True)

    def save(self, *args, **kwargs):
        # create slug as lowercase
        self.slug = slugify(self.name.lower())

        # save to db
        super(Post, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class RestaurantLocation(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name="locations")
    notes = models.TextField(max_length=150, blank=True)

    # https://docs.djangoproject.com/en/1.4/ref/contrib/localflavor/#united-states-of-america-us
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.city + self.state



class Restaurant(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, related_name="restaurants")
    managers = models.ManyToManyField(User, related_name="restaurants")
    phone = models.CharField(max_length=10, blank=True)

    def __unicode__(self):
        return self.name
