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

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['nombre', 'categoria', 'cantidad_stock', 'descripcion', 'preciou', 'unidad_medida', 'lead_time', 'agotado']

class PedidoClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PedidoCliente
        fields = ['folio', 'cliente', 'fecha', 'material', 'cantidad_pedida', 'compra_unica']

class OrdenCompraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = ['num_orden', 'fecha', 'material', 'cantidad_requerida']


