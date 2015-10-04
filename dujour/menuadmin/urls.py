from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dujour.menuadmin.views import MenuAdminIndexView, MenuAdminRestaurantView, MenuAdminMenuView

urlpatterns = [
    url(r'^$', login_required(MenuAdminIndexView.as_view()), name='menu_admin_index'),
    url(r'^restaurant/(?P<restaurant_id>[0-9]+)/$', login_required(MenuAdminRestaurantView.as_view()), name='menu_admin_restaurant'),
    url(r'^menu/(?P<pk>[0-9]+)/$', login_required(MenuAdminMenuView.as_view()), name='menu_admin_menu'),
]
