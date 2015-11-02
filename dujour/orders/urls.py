from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from dujour.orders.views import GraphicalOrderEntryView, TextOrderEntryView, AutoFillOrderEntryView, \
    HistoryOrderEntryView, CartView, UpdateOrderView, DeleteOrderView

urlpatterns = [
    url(r'^$', login_required(GraphicalOrderEntryView.as_view())),
    url(r'^graphical/$', login_required(GraphicalOrderEntryView.as_view()), name='graphical_place_order'),
    url(r'^text/$', login_required(TextOrderEntryView.as_view()), name='text_place_order'),
    url(r'^autofill/$', login_required(AutoFillOrderEntryView.as_view()), name='autofill_place_order'),
    url(r'^history/$', login_required(HistoryOrderEntryView.as_view()), name='history_place_order'),
    url(r'^cart/$', login_required(CartView.as_view()), name='cart'),
    url(r'^update/(?P<pk>[0-9]+)/$', login_required(UpdateOrderView.as_view()), name='update_order'),
    url(r'^delete/(?P<pk>[0-9]+)/$', login_required(DeleteOrderView.as_view()), name='delete_order'),
]
