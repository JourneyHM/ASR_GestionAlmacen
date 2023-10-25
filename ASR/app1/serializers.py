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
        fields = ['id', 'nombre', 'clave', 'ubicacion', 'categoria', 'cantidad_stock', 'unidad_medida']

class PedidoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = ['folio', 'cliente', 'fecha', 'material', 'cantidad_pedida', 'compra_unica']

class OrdenCompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = ['num_orden', 'proveedor', 'fecha', 'material', 'cantidad_requerida']


