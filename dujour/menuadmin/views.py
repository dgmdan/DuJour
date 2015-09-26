from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView

class MenuAdminIndexView(TemplateView):
    template_name = "menuadmin/index.html"
