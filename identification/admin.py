from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'phone', 'email', 'is_staff', 'date_joined')
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Персональная информация', {
            'fields': (
                'first_name',
                'last_name',
                'email',
                'phone',
            )
        }),
        ('Права', {
            'fields': (
                'groups',
                'user_permissions',
                'is_staff',
                'is_active',
                'is_superuser',
            )
        }),
        ('Даты', {
            'fields': (
                'date_joined',
                'last_login',
            )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)