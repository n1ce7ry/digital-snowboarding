from django.contrib import admin
from .models import *


@admin.register(Souvenirs)
class SouvenirsAdmin(admin.ModelAdmin):
    pass