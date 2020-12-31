
from django.urls import path

from .views import GetAllProduct, GetOneProduct, MainEditView, DeleteMainImage, UploadMainImage

urlpatterns = [
    path('all/', GetAllProduct.as_view(), name='get_all_product'),
    path('one_product/<id>/', GetOneProduct.as_view(), name='get_one_product'),
    path('main/update/<id>/', MainEditView.as_view()),
    path('one_product/<id>/', GetOneProduct.as_view(), name='get_one_product'),
    path('main/delete/<id>/', DeleteMainImage.as_view(), name='get_one_product'),
    path('main/post/', UploadMainImage.as_view(), name='get_one_product'),
]
