import re
from django import forms
from django.core.exceptions import ValidationError


class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=255,
                                 required=True,
                                 widget=forms.TextInput(attrs={
                                    'class': 'ticket-page__input',
                                    'pattern': '[А-Яа-я]{2,}',
                                    'placeholder': 'Иван',
                                 }),
                                 label='Введите имя:')
    email = forms.EmailField(max_length=255,
                             required=True,
                             widget=forms.TextInput(attrs={
                                'class': 'ticket-page__input',
                                'pattern': '([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,8})',
                                'placeholder': 'example@example.com',
                             }),
                             label='Введите почту:')
    phone = forms.CharField(max_length=255,
                            required=True,
                            widget=forms.TextInput(attrs={
                                'class': 'ticket-page__input',
                                'minlength':'11',
                                'pattern': '8[0-9]+',
                                'placeholder': 'Начиная с 8'
                            }),
                            label='Введите номер телефона:')
    seat_data = forms.CharField(max_length=255, required=False, widget=forms.HiddenInput(attrs={'id': 'seat_data'}))
    game_id = forms.CharField(max_length=255, required=False, widget=forms.HiddenInput(attrs={'id': 'game_id'}))


    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BookingForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['email'].initial = user.email
            self.fields['phone'].initial = user.phone


    def clean_email(self):
        email = self.cleaned_data.get('email')
        pattern = r"([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})"

        if not re.match(pattern, email):
            raise ValidationError('Введите электронную почту в верном формате')

        return email


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r"8[0-9]+"

        if not re.match(pattern, phone):
            raise ValidationError('Введите номер телефона в верном формате')

        return phone


    def clean_seat_data(self):
        seat_data = self.cleaned_data.get('seat_data')
        print(seat_data)
        if not seat_data:
            raise ValidationError('Выберите места')

        return seat_data