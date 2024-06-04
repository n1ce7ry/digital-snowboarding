import re
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


User = get_user_model()


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('home_page')
        else:
            return render(
                request,
                'indentification/login.html',
                context={'login_error': 'Введите корректные логин и пароль'}
            )


    return render(request, 'indentification/login.html')


def user_logout(request):
    logout(request)
    return redirect('home_page')


def registration(request):
    if request.method == 'POST':

        try:
            cleaned_data = validate_registration_data(request.POST)

        except ValidationError as error:
            return render(
                request,
                'indentification/registration.html',
                context={'registration_error': error.message, 'data': request.POST}
            )
        
        User.objects.create(
            username=cleaned_data['username'],
            password=make_password(cleaned_data['password']),
            phone=cleaned_data['phone'],
            email=cleaned_data['email'],
        )
        return redirect('login')


    return render(request, 'indentification/registration.html')


def validate_registration_data(registration_data):
    username = registration_data.get('username')
    password = registration_data.get('password'),
    repeated_password = registration_data.get('repeated_password'),
    phone = registration_data.get('phone')
    email = registration_data.get('email')

    validated_password = validate_password(
        password,
        repeated_password,
    )
    validated_phone = validate_phone(phone)
    validated_email = validate_email(email)

    return {
        'username': username,
        'password': validated_password,
        'phone': validated_phone,
        'email': validated_email,
    }


def validate_password(password, repeated_password):
    if password == repeated_password:
        return password
    
    raise ValidationError('Пароли не совпадают')


def validate_phone(phone):
    if len(phone) == 11:
        return phone
    
    raise ValidationError('Введите номер телефона в формате 89XXXXXXXX')


def validate_email(email):
    pattern = r'([A-Za-z0-9_.-]{1,})@([A-Za-z0-9_.-]{1,})\.([A-Za-z]{2,8})'
    if re.match(pattern, email):
        return email
    
    raise ValidationError('Введите корректный email')