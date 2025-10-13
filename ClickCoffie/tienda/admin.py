from django.contrib import admin
from .models import Categoria_producto
from .models import Inventario

admin.site.register(Categoria_producto)

@admin.register(Inventario)
class InventarioAdmin (admin.ModelAdmin):
    list_display = ('idProducto', 'Nombre', 'Categoria', 'Precio')
    search_fields = ('Nombre', 'Categoria')
