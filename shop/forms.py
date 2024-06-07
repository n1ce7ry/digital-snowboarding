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