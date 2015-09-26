from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dujour.menuadmin.views import MenuAdminIndexView

urlpatterns = [
    url(r'^$', login_required(MenuAdminIndexView.as_view()), name='menu_admin_index'),
]
