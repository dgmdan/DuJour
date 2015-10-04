from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from dujour.restaurants.models import Restaurant, Menu

class MenuAdminIndexView(ListView):
    template_name = 'menuadmin/index.html'
    model = Restaurant

class MenuAdminRestaurantView(ListView):
    template_name = 'menuadmin/restaurant.html'
    model = Menu

class MenuAdminMenuView(DetailView):
    template_name = 'menuadmin/menu.html'
    model = Menu

    def get_context_data(self, **kwargs):
        context = super(MenuAdminMenuView, self).get_context_data(**kwargs)
        # context['book_list'] = Book.objects.all()
        return context
