from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombre')
    descripcion = models.CharField(max_length= 200, null=True, blank=True, verbose_name='Descripción')

    def __str__ (self):
        return "Categoría: {}".format(self.nombre)

class Material(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombre')
    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_stock = models.PositiveIntegerField(null=True, blank=True, verbose_name='Cantidad en stock')
    descripcion = models.CharField(max_length= 200, null=True, blank=True, verbose_name='Descripción')
    preciou = models.FloatField(null=True, blank=True, verbose_name='Precio Unitario')
    unidad_medida = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unidad de Medida')
    lead_time = models.CharField(max_length=50, null=True, blank=True, verbose_name='Tiempo de retorno')
    agotado = models.BooleanField(default=False, verbose_name='¿Está Agotado?')

    def __str__ (self):
        return "Material: {}".format(self.nombre)

class PedidoCliente(models.Model):
    folio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Folio')
    cliente = models.CharField(max_length=100, null=True, blank=True, verbose_name='Cliente')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_pedida = models.PositiveIntegerField(default=0, verbose_name='Cantidad pedida')
    compra_unica = models.BooleanField(default=True, verbose_name='¿Es compra única?')
    fecha = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='Fecha')

    def __str__ (self):
        return "Pedido del Cliente: {} - {} - {}".format(self.folio, self.cliente, self.fecha)

class OrdenCompra(models.Model):
    num_orden = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número de orden')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_requerida =  models.PositiveIntegerField(default=0, verbose_name='Cantidad requerida')
    fecha = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='Fecha')
    
    def __str__ (self):
        return "Orden de compra: {} - {}".format(self.num_orden, self.fecha)







