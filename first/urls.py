from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import GetMainProduct, send_view


urlpatterns = [
    # path('page/', GetMainProduct.as_view(), name='first_page'),  # в процессе
    path('contact/', csrf_exempt(send_view), name='contact')
]