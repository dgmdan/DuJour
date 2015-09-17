from django.shortcuts import render
from django.views.generic.base import TemplateView

class OrderFormView(TemplateView):
    template_name = "mainsite/order_form.html"
