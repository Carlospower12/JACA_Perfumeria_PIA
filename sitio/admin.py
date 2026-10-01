from django.contrib import admin
from .models import Perfume, ArchivoSubido

@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ("nombre","marca","categoria","precio","disponible")
    list_filter = ("marca","categoria","disponible")
    search_fields = ("nombre","marca","descripcion")

@admin.register(ArchivoSubido)
class ArchivoSubidoAdmin(admin.ModelAdmin):
    list_display = ("nombre","fecha")
