from decimal import Decimal
from django.conf import settings
from .models import Souvenir


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def __iter__(self):
        souvenir_ids = self.cart.keys()
        souvenirs = Souvenir.objects.filter(id__in=souvenir_ids)
        for souvenir in souvenirs:
            self.cart[str(souvenir.id)]['souvenir'] = souvenir

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def add(self, souvenir, quantity=1, update_quantity=False):
        souvenir_id = str(souvenir.id)
        if souvenir_id not in self.cart:
            self.cart[souvenir_id] = {'quantity': 0,
                                     'price': str(souvenir.price)}
        if update_quantity:
            self.cart[souvenir_id]['quantity'] = quantity
        else:
            self.cart[souvenir_id]['quantity'] += quantity
        self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def remove(self, souvenir):
        souvenir_id = str(souvenir.id)
        if souvenir_id in self.cart:
            del self.cart[souvenir_id]
            self.save()


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())


    def get_total_quanity(self):
        return sum(item['quantity'] for item in self.cart.values())


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True