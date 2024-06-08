from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Souvenir, SouvenirType, OrderItem
from .cart import Cart
from .forms import CartAddSouvenirForm, CheckoutForm
from django.contrib.auth import get_user_model


User = get_user_model()


def shop(request):
    souvenirs = Souvenir.objects.all()
    favorite_souvenirs = User.objects.get(id=request.user.id).favorite_souvenirs.all()
    souvenirs_types = SouvenirType.objects.all()
    cart_souvenir_form = CartAddSouvenirForm()
    return render(
        request,
        'shop/shop.html',
        context={'souvenirs': souvenirs,
                 'cart_souvenir_form': cart_souvenir_form,
                 'souvenirs_types': souvenirs_types,
                 'favorite_souvenirs': favorite_souvenirs}
    )


@require_POST
def cart_add(request, souvenir_id):
    cart = Cart(request)
    souvenir = get_object_or_404(Souvenir, id=souvenir_id)
    form = CartAddSouvenirForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(souvenir=souvenir,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, souvenir_id):
    cart = Cart(request)
    souvenir = get_object_or_404(Souvenir, id=souvenir_id)
    cart.remove(souvenir)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = cart.get_total_price()
            if request.user.is_authenticated:
                order.user = request.user

            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         souvenir=item['souvenir'],
                                         price=item['price'],
                                         quantity=item['quantity'])
        
            cart.clear()
            return render(request, 'shop/created.html',
                          {'order': order})

    form = CheckoutForm(instance=request.user if request.user.is_authenticated else None)

    return render(
        request,
        'shop/cart-detail.html',
        {'cart': cart, 'form': form}
    )


def clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')