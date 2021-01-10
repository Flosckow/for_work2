from django import forms

from .models import MainProduct


class MainProductForm(forms.ModelForm):
    class Meta:
        model = MainProduct
        fields = '__all__'


class SendEmail(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.CharField(label='Тема', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)