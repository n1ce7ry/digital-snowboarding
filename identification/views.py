from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UserRegistrationForm, UserResetPassword
from django.contrib.auth import update_session_auth_hash


User = get_user_model()


@login_required
def reset_password(request):
    if request.method == 'POST':
        form = UserResetPassword(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            update_session_auth_hash(request, user)
            return redirect('edit-profile')
        else:
            return render(
                request,
                'identification/reset_password.html',
                context={'form': form}
            )

    form = UserResetPassword()

    return render(request, 'identification/reset_password.html', context={'form': form})


@login_required
def profile(request):
    return render(request, 'identification/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(
                request,
                'identification/edit_profile.html',
                context={'form': form}
            )

    form = UpdateUserForm(instance=request.user)

    return render(request, 'identification/edit_profile.html', context={'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home_page')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return redirect('profile')
        else:
            return render(
                request,
                'identification/login.html',
                context={'login_error': 'Введите корректные логин и пароль'}
            )


    return render(request, 'identification/login.html')


def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            return render(request, 'identification/registration.html', context={'form': form})

    form = UserRegistrationForm()

    return render(request, 'identification/registration.html', context={'form': form})