from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
import datetime

from dujour.orders.forms import AddItemForm
from dujour.restaurants.models import Restaurant, DayRestaurant, MenuItemRegion, Menu

class GraphicalOrderEntryView(FormView):
    template_name = 'orders/graphical_entry.html'
    form_class = AddItemForm

    def get_context_data(self, **kwargs):
        context = super(GraphicalOrderEntryView, self).get_context_data(**kwargs)
        restaurant = DayRestaurant.objects.get(day_of_week=datetime.datetime.today().weekday()).restaurant
        menu = Menu.objects.get(restaurant=restaurant)
        context['object'] = menu
        context['region_list'] = MenuItemRegion.objects.filter(menu_item__menu=menu)
        return context

    def form_valid(self, form):
        form.add_item(self.request.user)
        return JsonResponse({'status': 'success'})

    def form_invalid(self, form):
        return JsonResponse(form.errors, status=400)
