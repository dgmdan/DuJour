from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import View
from social_auth.exceptions import AuthFailed
from social_auth.views import complete

class OrderFormView(TemplateView):
    template_name = "mainsite/order_form.html"


class AuthComplete(View):
    def get(self, request, *args, **kwargs):
        backend = kwargs.pop('backendp')
        try:
            return complete(request, backend, *args, **kwargs)
        except AuthFailed:
            messages.error(request, "Your Google Apps domain isn't authorized for this app")
            return HttpResponseRedirect(reverse('login'))


class LoginError(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=401)