from django.db import models
from django.core.exceptions import ValidationError
import os


class Order(models.Model):
    is_placed = models.BooleanField(default=True)
    user = models.ForeignKey
    body = models.CharField(max_length=255)


    def __str__(self):
        return self.body

