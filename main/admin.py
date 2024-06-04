from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):


    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.photo.url))
        #return format_html(f'<img src="{obj.photo.url}" style="max-width:200px; max-height:200px"/>')


    list_display = ['id', 'image_tag',]


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