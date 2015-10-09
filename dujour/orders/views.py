from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from dujour.orders.forms import AddItemForm

class GraphicalOrderEntryView(FormView):
    template_name = 'orders/graphical_entry.html'
    form_class = AddItemForm

    def get(self, request, *args, **kwargs):
        return super(GraphicalOrderEntryView, self).get(request, args, kwargs)

    def form_valid(self, form):
        pk = form.add_item()
        if self.request.is_ajax():
            return JsonResponse({'status': 'success', 'pk': pk})
        else:
            return super(GraphicalOrderEntryView, self).form_valid(form)
