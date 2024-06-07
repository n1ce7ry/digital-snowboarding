from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):

    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-width:200px; max-height:200px">')

    preview.short_description = 'Превью'


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