from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

from dujour.mainsite.views import OrderFormView

urlpatterns = [
    url(r'^$', login_required(OrderFormView.as_view()), name='home'),
    url(r'^menuadmin/', include('dujour.menuadmin.urls')),
    url(r'^orders/', include('dujour.orders.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
