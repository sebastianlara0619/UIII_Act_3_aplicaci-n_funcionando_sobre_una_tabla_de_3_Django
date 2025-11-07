from django.contrib import admin
from .models import Proveedor, Producto, Producto_Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'telefono', 'email', 'ciudad', 'fecha_registro')
    search_fields = ('nombre', 'empresa', 'ciudad')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'precio_venta', 'stock', 'fecha_ingreso')
    search_fields = ('nombre', 'marca', 'modelo')

@admin.register(Producto_Proveedor)
class ProductoProveedorAdmin(admin.ModelAdmin):
    list_display = ('producto', 'proveedor', 'precio_compra', 'cantidad_disponible', 'fecha_entrega')
    list_select_related = ('producto', 'proveedor')
