from django import forms

from dujour.restaurants.models import Menu, MenuItem, MenuItemRegion

class CreateItemAndRegionForm(forms.Form):
    menu_id = forms.IntegerField()
    sw_lat = forms.FloatField()
    sw_lng = forms.FloatField()
    ne_lat = forms.FloatField()
    ne_lng = forms.FloatField()
    menu_item_name = forms.CharField(max_length=255)
    menu_item_price = forms.DecimalField()

    def create_item_and_region(self):
        menu = Menu.objects.get(pk=self.cleaned_data['menu_id'])
        menu_item, menu_item_created = MenuItem.objects.get_or_create(menu=menu, name=self.cleaned_data['menu_item_name'],
                                                                      price=self.cleaned_data['menu_item_price'])
        menu_item_region = MenuItemRegion.objects.create(menu_item=menu_item, sw_lng=self.cleaned_data['sw_lng'],
                                                         sw_lat=self.cleaned_data['sw_lat'], ne_lng=self.cleaned_data['ne_lng'], 
                                                         ne_lat=self.cleaned_data['ne_lat'])
        return menu_item_region.id
