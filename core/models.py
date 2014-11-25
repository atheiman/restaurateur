from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify



MARKDOWN_HELP_TEXT = "This field supports <a href='http://daringfireball.net/projects/markdown/basics' target='blank'>markdown formatting</a>."



class Category(models.Model):
    name = models.CharField(max_length=75, unique=True)
    slug = models.SlugField(max_length=75, unique=True)
    plain_text_description = models.TextField(max_length=250, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'categories'

    def save(self, *args, **kwargs):
        # create slug as lowercase
        self.slug = slugify(self.name.lower())

        # save to db
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



class Restaurant(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    plain_text_description = models.TextField(max_length=500)
    markdown_description = models.TextField(max_length=500, blank=True, help_text=MARKDOWN_HELP_TEXT)
    category = models.ForeignKey('Category', related_name="restaurants")
    tags = models.ManyToManyField('Tag', blank=True)

    # managers are allowed to edit the info of a restaurant
    managers = models.ManyToManyField(User, related_name="restaurants")

    # phone to contact main office
    phone = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['name']

    def rating(self):
        """average of each locations' ratings"""
        total, count = 0.0, 0.0
        for l in self.locations:
            if l.rating is not None:
                total += l.rating
                count += 1
        return total/count

    def __unicode__(self):
        return self.name



class Tag(models.Model):
    slug = models.SlugField(max_length=75, unique=True)

    class Meta:
        ordering = ['slug']

    def save(self, *args, **kwargs):
        # create slug as lowercase
        self.slug = self.slug.lower()

        # save to db
        super(Tag, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.slug



class Special(models.Model):
    name = models.CharField(max_length=150)
    restaurant = models.ForeignKey('Restaurant', related_name="specials")
    plain_text_description = models.TextField(max_length=500, blank=True)

    published = models.BooleanField(default=True, help_text="Display this special on the site?")

    # days of week special is available
    mon = models.BooleanField(default=False)
    tue = models.BooleanField(default=False)
    wed = models.BooleanField(default=False)
    thu = models.BooleanField(default=False)
    fri = models.BooleanField(default=False)
    sat = models.BooleanField(default=False)
    sun = models.BooleanField(default=False)



class RestaurantLocation(models.Model):
    name = models.CharField(max_length=150)
    restaurant = models.ForeignKey('Restaurant', related_name="locations")
    plain_text_description = models.TextField(max_length=500, blank=True)

    # Contact info
    # https://docs.djangoproject.com/en/1.4/ref/contrib/localflavor/#united-states-of-america-us
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField(
        validators=[MaxValueValidator(99999), MinValueValidator(11111)]
    )
    phone = models.CharField(max_length=10, blank=True)

    class Meta:
        ordering = ['name']

    def rating(self):
        pass

    def __unicode__(self):
        return self.name



class Menu(models.Model):
    restaurant = models.ForeignKey('Restaurant', related_name="menus")

    # breakfast, lunch, dinner, drinks, dessert, etc.
    name = models.CharField(max_length=75)
    slug = models.SlugField(max_length=75)
    plain_text_description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        # create slug as lowercase
        self.slug = slugify(self.name.lower())

        # save to db
        super(Menu, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.restaurant.name + " " + self.name



class MenuItem(models.Model):
    menu = models.ForeignKey('Menu', related_name="items")
    name = models.CharField(max_length=75)
    plain_text_description = models.TextField(max_length=150, blank=True)

    price = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=2,
        max_digits=5,
        validators=[MinValueValidator(0)],
    )
    spicy = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    allergies = models.CharField(max_length=75, blank=True)

    class Meta:
        ordering = ['name']

    def rating(self):
        pass

    def __unicode__(self):
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User)

    date = models.DateField(auto_now=True)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    comment = models.TextField(max_length=250, blank=True)

    class Meta:
        ordering = ['date']

    def __unicode__(self):
        return self.id



class LocationReview(Review):
    location = models.ForeignKey(RestaurantLocation, related_name='location_reviews')



class MenuItemReview(Review):
    menu_item = models.ForeignKey(MenuItem, related_name='menu_item_reviews')
