from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from testovoe_work import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', include('first.urls')),
    path('main/', include('main.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)