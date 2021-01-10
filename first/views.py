from django.views.generic import TemplateView

from main.models import Product
from .models import MainProduct
from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render

from django.views import View
from testovoe_work.settings import EMAIL_HOST_USER


class GetMainProduct(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_product'] = MainProduct.objects.first()
        context["product"] = Product.objects.all().order_by('-created')
        return context


def send_view(request):
    rpg = request.POST.get
    if request.method == 'POST':
        subject = rpg("subject")
        from_email = rpg("from_email")
        message = rpg("message")
        try:
            send_mail(f'{subject}', message, EMAIL_HOST_USER, [EMAIL_HOST_USER]) #
        except BadHeaderError:
            return HttpResponse('Ошибка в теме письма')
    else:
        return HttpResponse('Неверный запрос')
    return HttpResponse('Успешно')