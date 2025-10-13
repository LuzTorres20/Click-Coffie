from django.db import models

class Categoria_producto (models.Model):
    idCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField(max_length=100)

    def __str__(self):
        return self.NombreCategoria

class Inventario (models.Model):

    idProducto = models.AutoField(primary_key= True)
    Nombre = models.CharField(max_length=100)
    Categoria = models.ForeignKey(Categoria_producto, on_delete=models.CASCADE, related_name='inventarios', null=False, blank=False,)
    Precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.Nombre
    