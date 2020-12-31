from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect, JsonResponse
from django.template.loader import render_to_string
from django.views import View

from .models import Product, MainProduct
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .forms import MainProductForm, ProductForm

# from utils import send_email


def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['youknowhowwhoiam@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('main/')
    else:

        return HttpResponse('Make sure all fields are entered and valid.')


class GetAllProduct(ListView):
    model = Product


class SendEmail(View):

    def post(self, request):
        if request.method == "POST":
            return send_email()
        else:
            return HttpResponse('Error')


class GetOneProduct(View):

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return product


class MainEditView(UpdateView):
    # specify the model you want to use
    model = MainProduct

    # specify the fields
    fields = [
        "title",
        "description",
        "image"
    ]

    success_url = "main/"


class ProductEditView(UpdateView):
    model = Product

    fields = '__all__'
    success_url = 'main/'


class DeleteMainImage(DeleteView):
    model = MainProduct
    fields = ['image']
    success_url = 'main/'


class UploadMainImage(CreateView):
    model = MainProduct
    form_class = MainProductForm








