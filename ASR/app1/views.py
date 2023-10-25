from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from ASR.app1.serializers import UserSerializer, GroupSerializer
from .serializers import *


def dashboard(request):
    return render(request, "app1/index.html")

def stock(request):
    materiales = list(Material.objects.all())
    ctx = {'materiales':materiales}
    return render(request, "app1/stock.html", ctx)

def ordenesList(request):
    ordenes = list(OrdenCompra.objects.all())
    pedidos = list(PedidoCliente.objects.all())
    ctx = {"ordenes": ordenes, "pedidos":pedidos}
    return render(request, "app1/ordenes_pedidos-list.html", ctx)

def buttons(request):
    return render(request, "app1/ui-buttons.html")

def cards(request):
    return render(request, "app1/ui-card.html")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset  = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class PedidoClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = PedidoCliente.objects.all()
    serializer_class = PedidoClienteSerializer

class OrdenCompraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that MyModel to be viewed or edited.
    """
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer


    
