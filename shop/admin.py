from django.contrib import admin
from .models import *


@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
    pass


@admin.register(SouvenirType)
class SouvenirTypeAdmin(admin.ModelAdmin):
    pass


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'email',
                    'address', 'paid',
                    'created_at', 'updated']
    list_filter = ['paid', 'created_at', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)