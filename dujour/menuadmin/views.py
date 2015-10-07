from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from dujour.restaurants.models import Restaurant, Menu, MenuItem, MenuItemRegion
from dujour.menuadmin.forms import CreateItemAndRegionForm

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
        context['region_list'] = MenuItemRegion.objects.filter(menu_item__menu__id=self.object.id)
        return context


class CreateItemAndRegionView(FormView):
    form_class = CreateItemAndRegionForm

    def form_valid(self, form):
        pk = form.create_item_and_region()
        if self.request.is_ajax():
            return JsonResponse({'status': 'success', 'pk': pk})
        else:
            return super(CreateItemAndRegionView, self).form_valid(form)
