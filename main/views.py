from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from shop.models import Souvenir
from shop.forms import CartAddSouvenirForm


User = get_user_model()


def home_page(request):
    return render(request, 'main/home_page.html')


@login_required
def favorite_souvenirs(request):
    favorite_souvenirs = User.objects.get(id=request.user.id).favorite_souvenirs.all()
    cart_souvenir_form = CartAddSouvenirForm()
    return render(
        request,
        'main/favorite.html',
        context={'favorite_souvenirs': favorite_souvenirs, 'cart_souvenir_form': cart_souvenir_form})


@login_required
def add_favorite_souvenirs(request, souvenir_id):
    Souvenir.objects.get(id=souvenir_id).users.add(request.user.id)
    return redirect('favorite_souvenirs')


@login_required
def del_favorite_souvenirs(request, souvenir_id):
    Souvenir.objects.get(id=souvenir_id).users.remove(request.user.id)
    return redirect('favorite_souvenirs')