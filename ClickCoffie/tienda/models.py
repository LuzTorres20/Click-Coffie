from django.db import models

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
    