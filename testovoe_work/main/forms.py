from django import forms
from .models import MainProduct, Product


class MainProductForm(forms.ModelForm):
    class Meta:
        model = MainProduct
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
