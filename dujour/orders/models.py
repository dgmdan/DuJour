from django.db import models
from django.contrib.auth.models import User

from dujour.restaurants.models import MenuItem


class Order(models.Model):
    order_date = models.DateField()
    user = models.ForeignKey(User)
    menu_item = models.ForeignKey(MenuItem, null=True)
    quantity = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.menu_item.name

    def extended_price(self):
        return self.quantity * self.menu_item.price
