from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['nombre', 'cantidad_stock', 'descripcion', 'preciou', 'unidad_medida', 'lead_time', 'agotado']

class PedidoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = ['folio', 'cliente', 'material', 'cantidad_pedida', 'compra_unica']

class OrdenCompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = ['num_orden', 'material', 'cantidad_requerida']

class AlmacenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Almacen
        fields = ['stock', 'ordencompra', 'pedidocliente']

