from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dujour.menuadmin.views import MenuAdminIndexView, MenuAdminRestaurantView, MenuAdminMenuView, CreateItemAndRegionView, \
	UpdateItemAndRegionView, DeleteItemAndRegionView, LoadRegionView

urlpatterns = [
    url(r'^$', login_required(MenuAdminIndexView.as_view()), name='menu_admin_index'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', login_required(MenuAdminRestaurantView.as_view()), name='menu_admin_restaurant'),
    url(r'^menu/(?P<pk>[0-9]+)/$', login_required(MenuAdminMenuView.as_view()), name='menu_admin_menu'),
    url(r'^create_item_and_region/$', login_required(CreateItemAndRegionView.as_view()), name='menu_admin_create_item_and_region'),
    url(r'^update_item_and_region/$', login_required(UpdateItemAndRegionView.as_view()), name='menu_admin_update_item_and_region'),
    url(r'^delete_item_and_region/$', login_required(DeleteItemAndRegionView.as_view()), name='menu_admin_delete_item_and_region'),
    url(r'^load_region/$', login_required(LoadRegionView.as_view()), name='menu_admin_load_region'),
]
