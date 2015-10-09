from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dujour.orders.views import GraphicalOrderEntryView

urlpatterns = [
    url(r'^$', login_required(GraphicalOrderEntryView.as_view()), name='graphical_place_order'),
]
