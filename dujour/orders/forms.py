import datetime
from django import forms

from dujour.orders.models import Order, MenuItem

class AddItemForm(forms.Form):
    menu_item_id = forms.IntegerField()
    quantity = forms.IntegerField()
    comments = forms.CharField(required=False)

    def add_item(self, user):
        menu_item = MenuItem.objects.get(pk=self.cleaned_data['menu_item_id'])
        order = Order.objects.create(order_date=datetime.date.today(),
                                     user=user,
                                     menu_item=menu_item,
                                     quantity=self.cleaned_data['quantity'],
                                     comments=self.cleaned_data['comments'])
