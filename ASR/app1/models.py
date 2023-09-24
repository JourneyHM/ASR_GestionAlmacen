from django.db import models

# Create your models here.

class Material(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombre')
    cantidad_stock = models.PositiveIntegerField(null=True, blank=True, verbose_name='Cantidad en stock')
    descripcion = models.CharField(max_length= 100, null=True, blank=True, verbose_name='Descripción')
    preciou = models.FloatField(null=True, blank=True, verbose_name='Precio Unitario')
    unidad_medida = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unidad de Medida')
    lead_time = models.DateField(null=True, blank = True, verbose_name='Tiempo de retorno')
    agotado = models.BooleanField(default=False, verbose_name='¿Está Agotado?')

    def __str__ (self):
        return "Material: {}".format(self.nombre)

class PedidoCliente(models.Model):
    folio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Folio')
    cliente = models.CharField(max_length=100, null=True, blank=True, verbose_name='Cliente')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_pedida = models.PositiveIntegerField(default=0, verbose_name='Cantidad pedida')
    compra_unica = models.BooleanField(default=True, verbose_name='¿Es compra única?')

    def __str__ (self):
        return "Pedido del Cliente: {} - {}".format(self.folio, self.cliente)

class OrdenCompra(models.Model):
    num_orden = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número de orden')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_requerida =  models.PositiveIntegerField(default=0, verbose_name='Cantidad requerida')
    def __str__ (self):
        return "Orden de compra: {}".format(self.num_orden)

class Almacen(models.Model):
    stock = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    ordencompra =  models.ForeignKey(OrdenCompra, null=True, blank=True, on_delete=models.CASCADE)
    pedidocliente =  models.ForeignKey(PedidoCliente, null=True, blank=True, on_delete=models.CASCADE)






