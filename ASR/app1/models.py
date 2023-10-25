from django.db import models
from django.utils import timezone

# Create your models here.

class Material(models.Model):
    OPCIONES_CATEGORIA = [
        ('Hule', 'Productos de Hule'),
        ('Polietileno', 'Polietileno'),
        ('Extruido', 'Extruido'),
        ('Cintas', 'Cintas'),
        ('Espumas Autoadheribles', 'Espumas Autoadheribles'),
        ('Piezas Troqueladas', 'Piezas Troqueladas'),
        ('Empaque', 'Productos para Empaque'),
        ('Juntas Metálicas', 'Juntas Metálicas'),
        ('Aislamientos Térmicos', 'Aislamientos Térmicos'),
        ('Sellos Empaques', 'Sellos o Empaques'),
        ('Unicel', 'Productos de Unicel'),
        ('Polifom', 'Polifom'),
        ('Poliburbuja', 'Poliburbuja'),
        ('Fibra de Vidrio', 'Fibra de Vidrio'),
        ('Cordon', 'Cordon'),
        ('PTFE', 'Productos PTFE'),
        ('Especiales', 'Productos Especiales'),
    ]
    nombre = models.CharField(max_length=50, null=True, blank=True, verbose_name='Nombre')
    clave = models.CharField(max_length=50, null=True, blank=True, verbose_name='Clave')
    ubicacion = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ubicación')
    categoria = models.CharField(max_length=25, choices=OPCIONES_CATEGORIA,default='Hule', verbose_name='Categoría')
    cantidad_stock = models.PositiveIntegerField(null=True, blank=True, verbose_name='Cantidad en stock')
    unidad_medida = models.CharField(max_length=50, null=True, blank=True, verbose_name='Unidad de Medida')

    def __str__ (self):
        return "{}".format(self.nombre)
    
    def actualizar_stock(self, cantidad_pedida):
        if cantidad_pedida > 0:
            self.cantidad_stock -= cantidad_pedida
            self.save()



class PedidoCliente(models.Model):
    folio = models.CharField(max_length=50, null=True, blank=True, verbose_name='Folio')
    cliente = models.CharField(max_length=100, null=True, blank=True, verbose_name='Cliente')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_pedida = models.PositiveIntegerField(default=0, verbose_name='Cantidad pedida')
    compra_unica = models.BooleanField(default=True, verbose_name='¿Es compra única?')
    fecha = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='Fecha')

    def __str__ (self):
        return "Pedido del Cliente: {} - {} - {}".format(self.folio, self.cliente, self.fecha)
    
    def save(self, *args, **kwargs):
        super(PedidoCliente, self).save(*args, **kwargs)
        if self.compra_unica:
            self.material.actualizar_stock(self.cantidad_pedida)

class OrdenCompra(models.Model):
    num_orden = models.CharField(max_length=50, null=True, blank=True, verbose_name='Número de orden')
    proveedor = models.CharField(max_length=50, null=True, blank=True, verbose_name='Proveedor')
    material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    cantidad_requerida =  models.PositiveIntegerField(default=0, verbose_name='Cantidad requerida')
    fecha = models.DateTimeField(default=timezone.now, null=True, blank=True, verbose_name='Fecha')
    
    def __str__ (self):
        return "Orden de compra: {} - {}".format(self.num_orden, self.fecha)
    
    def save(self, *args, **kwargs):
        super(OrdenCompra, self).save(*args, **kwargs)
        self.material.cantidad_stock += self.cantidad_requerida
        self.material.save()







