from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    if not (value.name.endswith('.png') or value.name.endswith('.jpg')):
        raise ValidationError(u'Please upload a PNG or JPG file only')

class Restaurant(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    website = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class DayRestaurant(models.Model):
    class Meta:
        verbose_name = 'Assigned day of week'
        verbose_name_plural = 'Assigned days of week'

    DAY_CHOICES = (
        (0, 'Sunday'),
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
        (6, 'Saturday'),
    )
    restaurant = models.ForeignKey(Restaurant)
    day_of_week = models.IntegerField(choices=DAY_CHOICES)

class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    file = models.FileField(upload_to='static/menus/', validators=[validate_file_extension])
