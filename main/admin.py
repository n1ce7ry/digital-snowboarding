from .models import *
from django import forms
from django.contrib import admin
from django.utils.html import format_html


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    def image_id(self, obj):
        return f'Фото №{obj.id}'

    def image_preview(self, obj):
        return format_html(f'<img src="{obj.photo.url}" style="max-width:200px; max-height:200px"/>')

    image_id.short_description = 'ID'
    image_preview.short_description = 'Превью'

    list_display = ['image_id', 'image_preview']


class FactsInline(admin.StackedInline):
    model = InterestingFactAboutPlayer
    max_num = 2
    extra = 0


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('full_name',),}
    inlines = [FactsInline,]


    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'quote':
            kwargs['widget'] = forms.Textarea(attrs={'rows': 8, 'cols': 45})
        return super().formfield_for_dbfield(db_field, **kwargs)
    

@admin.register(InterestingFactAboutPlayer)
class InterestingFactAboutPlayerAdmin(admin.ModelAdmin):
    pass


@admin.register(GameSchedule)
class GameScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass


@admin.register(MailingList)
class MailingAdmin(admin.ModelAdmin):
    pass