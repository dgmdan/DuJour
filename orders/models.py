from django.db import models
from django.core.exceptions import ValidationError
import os

def valid_order(value):
	if not value.body:
		raise ValidationError(u'Please enter your order')

class Order(models.Model):
    is_placed = models.BooleanField(default=True)
    user = models.CharField(max_length=200)
    body = models.CharField(max_length=255)
    soup_type = models.CharField(max_length=200, blank=True)
    soup_size = models.CharField(max_length=20, blank=True)
    notes = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.body

