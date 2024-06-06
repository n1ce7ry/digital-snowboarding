from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:souvenir_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:souvenir_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.clear, name='clear'),
    path('', views.shop, name='shop'),
]