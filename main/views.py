from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from shop.models import Souvenir
from shop.forms import CartAddSouvenirForm
from django.http import JsonResponse


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


@require_POST
@login_required
def add_favorite_souvenirs(request, souvenir_id):
    souvenir = get_object_or_404(Souvenir, id=souvenir_id)
    souvenir.users.add(request.user.id)
    return JsonResponse({'success': 'success', 'souvenir': souvenir.name,
                         'souvenir_id': souvenir.id})


@login_required
def del_favorite_souvenirs(request, souvenir_id):
    Souvenir.objects.get(id=souvenir_id).users.remove(request.user.id)
    return redirect('favorite_souvenirs')