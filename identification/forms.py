from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'phone']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=11, min_length=11, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']


class UserResetPassword(forms.ModelForm):
    old_password = forms.CharField(max_length=200, required=True)
    new_password = forms.CharField(max_length=200, required=True)
    repeated_new_password = forms.CharField(max_length=200, required=True)

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

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'repeated_new_password']