from pprint import pprint

from django.http import HttpResponse
from django.shortcuts import render

from django.views import View

from first.models import MainProduct
from .models import Product, ListTitle
from django.views.generic import ListView, UpdateView, TemplateView


class GetAllProduct(TemplateView):
    template_name = "base_product_list.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all().order_by("-created")
        context["main_product"] = MainProduct.objects.first()
        return context


class GetOneProduct(View):
    def get(self, request, id):

        product = Product.objects.get(pk=id)
        list_title = ListTitle.objects.all()

        context = {'product': product,
                   'list_title': list_title}

        return render(request, 'product.html', context)


class ProductEditView(UpdateView):
    model = Product

    fields = '__all__'
    success_url = 'main/'









