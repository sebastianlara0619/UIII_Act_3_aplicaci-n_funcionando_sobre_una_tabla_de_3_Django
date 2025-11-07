# app_Venta_Telefonos/models.py
from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.empresa})"


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now_add=True)

    # Relación muchos a muchos con proveedores a través de Producto_Proveedor
    proveedores = models.ManyToManyField(Proveedor, through='Producto_Proveedor', related_name='productos')

    def __str__(self):
        return f"{self.nombre} - {self.marca} ({self.modelo})"


class Producto_Proveedor(models.Model):
    # Referencia al producto y al proveedor (modelo intermedio)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='producto_proveedores')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos_proveedor')

    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField()
    garantia_meses = models.PositiveIntegerField(default=12)
    fecha_entrega = models.DateField()

    # (Opcional) algún campo extra, por ejemplo número de lote
    lote = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.producto.marca} {self.producto.modelo} - {self.proveedor.empresa}"
