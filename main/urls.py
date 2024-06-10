from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('team/<slug:team_slug>', views.team, name='team'),
    path('player/<slug:player_slug>', views.player, name='player'),
    path('teams/', views.teams, name='teams'),
    path('tournament-schedule/', views.tournament_schedule, name='tournament_schedule'),
    path('favorite/', views.favorite_souvenirs, name='favorite_souvenirs'),
    path('add-favorite/<int:souvenir_id>', views.add_favorite_souvenirs, name='add_favorite_souvenirs'),
    path('del-favorite/<int:souvenir_id>', views.del_favorite_souvenirs, name='del_favorite_souvenirs'),
]