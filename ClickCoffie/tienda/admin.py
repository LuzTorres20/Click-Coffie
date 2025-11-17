from django.contrib import admin
from .models import CarritoItem, Categoria_producto
from .models import Inventario
from django.utils.html import mark_safe

admin.site.register(Categoria_producto)

@admin.register(Inventario)
class InventarioAdmin (admin.ModelAdmin):
    list_display = ('idProducto', 'imagen_tag','Nombre', 'Categoria', 'Precio',  'CantidadActual' )
    search_fields = ('Nombre', 'Categoria')
    list_filter = ('Categoria',)

    def imagen_tag(self, obj):
            if obj.Imagen:
                return mark_safe(f'<img src="{obj.Imagen.url}" width="50" height="50" />')
            return "-"
    imagen_tag.short_description = 'Imagen'

@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'producto', 'cantidad', 'vendido', 'fecha_creacion')
    list_filter = ('usuario',)