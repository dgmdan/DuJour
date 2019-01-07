from django.db import models
from django.contrib.auth.models import User

from dujour.restaurants.models import MenuItem, Restaurant, MenuItemTypeOption


class Order(models.Model):
    order_date = models.DateField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE)
    menu_item = models.ForeignKey('restaurants.MenuItem', null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.menu_item.name

    def extended_price(self):
        return self.quantity * self.menu_item.price

class OrderMenuItemTypeOption(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    menu_item_type_option = models.ForeignKey('restaurants.MenuItemTypeOption', on_delete=models.CASCADE)
