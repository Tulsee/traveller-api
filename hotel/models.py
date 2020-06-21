from django.db import models
import random


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9999)
    return 'hotel/{title}/{file}'.format(title=instance.title, file=filename)


def upload_image_path_other(instance, filename):
    new_filename = random.randint(1, 9999)
    return 'hotel/{title}/secondary/{file}'.format(title=instance.title, file=filename)


class Hotel(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    email = models.EmailField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True, null=True)
    contact = models.BigIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, default='NEPAL')
    city = models.CharField(max_length=100, blank=True, default='KATHMANDU')
    street = models.CharField(max_length=50, blank=True)
    photo_main = models.ImageField(upload_to=upload_image_path, blank=True)
    photo_1 = models.ImageField(upload_to=upload_image_path_other, blank=True)
    photo_2 = models.ImageField(upload_to=upload_image_path_other, blank=True)
    photo_3 = models.ImageField(upload_to=upload_image_path_other, blank=True)
    photo_4 = models.ImageField(upload_to=upload_image_path_other, blank=True)
    photo_5 = models.ImageField(upload_to=upload_image_path_other, blank=True)

    def __str__(self):
        return self.title


class Facility(models.Model):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    wifi = models.BooleanField(default=True)
    parking = models.BooleanField(default=True)
    airport_pickup = models.BooleanField(default=True)
    fitness_center = models.BooleanField(default=True)
    swimming_pool = models.BooleanField(default=True)
    spa = models.BooleanField(default=True)
    restaurant = models.BooleanField(default=True)
    wheelchair_access = models.BooleanField(default=True)
    business_center = models.BooleanField(default=True)
    casino = models.BooleanField(default=True)
    bar_lounge = models.BooleanField(default=True)
    busService_cab = models.BooleanField(default=True)
    children_activity = models.BooleanField(default=True)

    def __str__(self):
        return self.hotel.title+" facility details"
