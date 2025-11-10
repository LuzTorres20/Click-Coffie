from django.db import models
from django.contrib.auth.models import User

class Categoria_producto (models.Model):
    idCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.NombreCategoria

class Inventario (models.Model):

    idProducto = models.AutoField(primary_key= True)
    Nombre = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    Categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE, related_name='inventarios', null=False, blank=False,)
    Descripcion = models.CharField(max_length=100)
    Precio = models.DecimalField(max_digits=10, decimal_places=0)
    StockMinimo= models.IntegerField()
    CantidadActual= models.IntegerField()

    def __str__(self):
        return self.Nombre
    
class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    vendido = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)

    def subtotal(self):
        return self.producto.Precio * self.cantidad

    def __str__(self):
        return f"{self.usuario.username} - {self.producto.Nombre}"
    

