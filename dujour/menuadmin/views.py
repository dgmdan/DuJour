from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from dujour.restaurants.models import Restaurant, Menu, MenuItem, MenuItemRegion
from dujour.menuadmin.forms import CreateItemAndRegionForm, UpdateItemAndRegionForm, DeleteItemAndRegionForm

class MenuAdminIndexView(ListView):
    template_name = 'menuadmin/index.html'
    model = Restaurant

class MenuAdminRestaurantView(ListView):
    template_name = 'menuadmin/restaurant.html'
    model = Menu

    def get_queryset(self):
        return Menu.objects.filter(restaurant_id=self.kwargs['restaurant_id'])

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

class UpdateItemAndRegionView(FormView):
    form_class = UpdateItemAndRegionForm

    def form_valid(self, form):
        pk = form.update_item_and_region()
        if self.request.is_ajax():
            return JsonResponse({'status': 'success'})
        else:
            return super(UpdateItemAndRegionView, self).form_valid(form)

class DeleteItemAndRegionView(FormView):
    form_class = DeleteItemAndRegionForm

    def form_valid(self, form):
        pk = form.delete_item_and_region()
        if self.request.is_ajax():
            return JsonResponse({'status': 'success'})
        else:
            return super(DeleteItemAndRegionView, self).form_valid(form)

class LoadRegionView(View):
    def get(self, request):
        region = MenuItemRegion.objects.get(pk=request.GET.get('menu_item_region_id'))
        region_data = {'id': region.id, 'ne_lat': region.ne_lat, 'ne_lng': region.ne_lng, 'sw_lat': region.sw_lat, 'sw_lng': region.sw_lng}
        menu_item_data = {'name': region.menu_item.name, 'price': region.menu_item.price}
        return JsonResponse({'data': {'region': region_data, 'menu_item': menu_item_data}})
