from django.views.generic.base import TemplateView

class OrderFormView(TemplateView):
    template_name = "mainsite/order_form.html"

    def get_context_data(self, **kwargs):
        context = super(OrderFormView, self).get_context_data(**kwargs)
        context['user_first_name'] = self.request.user.first_name
        return context