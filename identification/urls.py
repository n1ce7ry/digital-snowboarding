from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('registration/', views.user_registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('reset-password/', views.reset_password, name='reset-password'),
]