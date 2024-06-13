from django import forms


class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=255, 
                                 widget=forms.TextInput(attrs={'class': 'ticket-page__input'}),
                                 label='Введите имя:')
    email = forms.CharField(max_length=255,
                            widget=forms.TextInput(
                                attrs={'class': 'ticket-page__input', 'pattern': '([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})'}
                            ),label='Введите почту:')
    phone = forms.CharField(max_length=255,
                            widget=forms.TextInput(
                                attrs={'class': 'ticket-page__input', 'minlength':'11', 'pattern': '\8[0-9]+'}
                            ), label='Введите номер телефона:')
    seat_data = forms.CharField(max_length=255, widget=forms.HiddenInput(attrs={'id': 'seat_data'}))