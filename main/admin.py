from django.contrib import admin
from django.utils.html import format_html
from .models import *


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    def image_id(self, obj):
        return f'Фото №{obj.id}'

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-width:200px; max-height:200px"/>')

    image_id.short_description = 'ID'
    image_preview.short_description = 'Превью'

    list_display = ['image_id', 'image_preview']


class InterestingFactAboutPlayerAdmin(admin.ModelAdmin):
    pass


class FactsInline(admin.StackedInline):
    model = InterestingFactAboutPlayer
    max_num = 10
    extra = 0


class PlayerAdmin(admin.ModelAdmin):
    inlines = [FactsInline,]


admin.site.register(InterestingFactAboutPlayer, InterestingFactAboutPlayerAdmin)
admin.site.register(Player, PlayerAdmin)