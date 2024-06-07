from django import forms
from .models import Order


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddSouvenirForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int,
                                      initial=1, 
                                      widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'address', 'phone', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'backet-total__input'}),
            'address': forms.TextInput(attrs={'class': 'backet-total__input'}),
            'phone': forms.TextInput(attrs={'class': 'backet-total__input', 'minlength':'11', 'pattern': '\8[0-9]+'}),
            'email': forms.EmailInput(attrs={'class': 'backet-total__input', 'pattern': '([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})'}),
        }
        labels = {
            'first_name': 'Введите Ваше имя',
            'address': 'Введите Ваш адрес',
            'phone': 'Введите Ваш номер телефона',
            'email': 'Введите Вашу почту',
        }