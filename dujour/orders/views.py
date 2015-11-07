from django.core.urlresolvers import reverse
from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView
import datetime

from dujour.orders.forms import AddItemForm
from dujour.orders.models import Order
from dujour.restaurants.models import Restaurant, DayRestaurant, MenuItemRegion, Menu, MenuItem

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

class TextOrderEntryView(FormView):
    template_name = 'orders/text_entry.html'
    form_class = AddItemForm

    def get_success_url(self):
        return reverse('cart')

class AutoFillOrderEntryView(FormView):
    template_name = 'orders/autofill_entry.html'
    form_class = AddItemForm

    def get_success_url(self):
        return reverse('cart')

    def get_context_data(self, **kwargs):
        context = super(AutoFillOrderEntryView, self).get_context_data(**kwargs)
        restaurant = DayRestaurant.objects.get(day_of_week=datetime.datetime.today().weekday()).restaurant
        menu = Menu.objects.get(restaurant=restaurant)
        menu_items = MenuItem.objects.filter(menu=menu)
        context['menu_items'] = menu_items
        return context

    def form_valid(self, form):
        form.add_item(self.request.user)
        return super(AutoFillOrderEntryView, self).form_valid(form)

class HistoryOrderEntryView(FormView):
    template_name = 'orders/history_entry.html'
    form_class = AddItemForm

    def get_success_url(self):
        return reverse('cart')

    def get_context_data(self, **kwargs):
        context = super(HistoryOrderEntryView, self).get_context_data(**kwargs)
        restaurant = DayRestaurant.objects.get(day_of_week=datetime.datetime.today().weekday()).restaurant
        past_orders = Order.objects\
            .filter(user=self.request.user, menu_item__menu__restaurant=restaurant, order_date__lt=datetime.datetime.today())\
            .values('menu_item_id')\
            .annotate(times_ordered=Count('menu_item_id'))\
            .values('times_ordered', 'menu_item_id', 'menu_item__name', 'menu_item__price', 'comments')\
            .order_by('-times_ordered')[:5]
        context['past_orders'] = past_orders
        return context

    def form_valid(self, form):
        form.add_item(self.request.user)
        return super(HistoryOrderEntryView, self).form_valid(form)

class CartView(ListView):
    template_name = 'orders/cart.html'
    model = Order

    def get_queryset(self):
        orders = Order.objects.filter(user=self.request.user, order_date=datetime.date.today())
        return orders

class UpdateOrderView(UpdateView):
    model = Order
    fields = ('quantity', 'comments',)

    def get_success_url(self):
        return reverse('cart')

    def get_queryset(self):
        orders = super(UpdateOrderView, self).get_queryset()
        orders = orders.filter(user=self.request.user, order_date=datetime.date.today())
        return orders

class DeleteOrderView(DeleteView):
    model = Order

    def get_success_url(self):
        return reverse('cart')

    def get_queryset(self):
        orders = super(DeleteOrderView, self).get_queryset()
        orders = orders.filter(user=self.request.user, order_date=datetime.date.today())
        return orders
