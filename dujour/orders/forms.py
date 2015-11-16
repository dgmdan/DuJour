import datetime
from django import forms

from dujour.orders.models import Order, MenuItem
from dujour.restaurants.models import Restaurant

class AddItemForm(forms.Form):
    restaurant_id = forms.IntegerField()
    menu_item_id = forms.IntegerField(required=False)
    quantity = forms.IntegerField()
    comments = forms.CharField(required=False)

    def add_item(self, user):
        restaurant = Restaurant.objects.get(pk=self.cleaned_data['restaurant_id'])
        menu_item = None
        if self.cleaned_data['menu_item_id']:
            menu_item = MenuItem.objects.get(pk=self.cleaned_data['menu_item_id'])
        order = Order.objects.create(order_date=datetime.date.today(),
                                     user=user,
                                     restaurant=restaurant,
                                     menu_item=menu_item,
                                     quantity=self.cleaned_data['quantity'],
                                     comments=self.cleaned_data['comments'])
