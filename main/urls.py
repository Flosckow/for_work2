
from django.urls import path
from .views import GetOneProduct, GetAllProduct


urlpatterns = [
    path('all/', GetAllProduct.as_view(), name='get_one_product'), # работает
    path('one_product/<int:id>/', GetOneProduct.as_view(), name='get_one_product'), # работает
]
