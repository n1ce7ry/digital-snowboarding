from django.contrib import admin
from .models import *


@admin.register(Souvenir)
class SouvenirsAdmin(admin.ModelAdmin):
    pass