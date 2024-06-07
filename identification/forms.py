from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form__input user__registr', 'placeholder': 'Придумайте логин'}),
            'password': forms.PasswordInput(attrs={'class': 'form__input lock__registr', 'placeholder': 'Придумайте пароль'}),
            'email': forms.EmailInput(attrs={'class': 'form__input email__refistr', 'pattern': '([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})', 'placeholder': 'Введите E-mail'}),
            'phone': forms.TextInput(attrs={'class': 'form__input phone__registr', 'minlength':'11', 'pattern': '\8[0-9]+', 'placeholder': 'Введите телефон начиная с 8'}),
        }
        error_messages = {
            'email': {
                'unique': ("E-mail уже занят"),
            },
        }


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'edit-page__input', 'placeholder': 'Придумайте логин'}),
            'email': forms.EmailInput(attrs={'class': 'edit-page__input', 'pattern': '([A-z0-9_.-]{1,})@([A-z0-9_.-]{1,}).([A-z]{2,8})', 'placeholder': 'Введите E-mail'}),
            'phone': forms.TextInput(attrs={'class': 'edit-page__input', 'minlength':'11', 'pattern': '\8[0-9]+', 'placeholder': 'Введите телефон начиная с 8'}),
        }
        error_messages = {
            'email': {
                'unique': ("E-mail уже занят"),
            },
        }
        labels = {
            'username': 'Изменить логин',
            'email': 'Изменить email',
            'phone': 'Изменить телефон',
        }


class UserResetPassword(forms.ModelForm):
    old_password = forms.CharField(max_length=200, required=True)
    new_password = forms.CharField(max_length=200, required=True)
    repeated_new_password = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'repeated_new_password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["old_password"].label = "Введите старый пароль"
        self.fields["new_password"].label = "Введите новый пароль"
        self.fields["repeated_new_password"].label = "Повторите пароль"

        self.fields['old_password'].widget = forms.PasswordInput(
            attrs={'class': 'edit-page__input'}
        ) 
        self.fields['new_password'].widget = forms.PasswordInput(
            attrs={'class': 'edit-page__input'}
        ) 
        self.fields['repeated_new_password'].widget = forms.PasswordInput(
            attrs={'class': 'edit-page__input'}
        ) 

    def clean_repeated_new_password(self):
        if self.data['new_password'] != self.data['repeated_new_password']:
            raise forms.ValidationError('Пароли не совпадают')
        
        return self.cleaned_data

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not authenticate(username=user.username, password=old_password):
            raise forms.ValidationError('Неверный старый пароль')

        return old_password