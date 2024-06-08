from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('teams/', views.teams, name='teams'),
    path('favorite/', views.favorite_souvenirs, name='favorite_souvenirs'),
    path('add-favorite/<int:souvenir_id>', views.add_favorite_souvenirs, name='add_favorite_souvenirs'),
    path('del-favorite/<int:souvenir_id>', views.del_favorite_souvenirs, name='del_favorite_souvenirs'),
]