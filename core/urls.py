from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from rest_framework.documentation import include_docs_urls
from azbankgateways.urls import az_bank_gateways_urls

admin.autodiscover()

urlpatterns = [
    path('panel/', admin.site.urls),
    path('user/', include('UserManager.urls', namespace='UserManager')),
    path('api/', include('api.urls', namespace='api')),
    path('cdocs/', include_docs_urls(title='bse course')),
    path('bankgateways/', az_bank_gateways_urls()),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
