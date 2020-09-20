from rest_framework import serializers
from .models import (Menu,Factura,Mesa,Pedido,Platos,Cliente,Mesero)

class MenuSerializers(serializers.ModelSerializer):
   class Meta:
        model = Menu
        fields = ('__all__')

class FacturaSerializers(serializers.ModelSerializer):
   class Meta:
        model = Factura
        fields = ('__all__')

class MesaSerializers(serializers.ModelSerializer):
   class Meta:
        model = Mesa
        fields = ('__all__')

class PedidoSerializers(serializers.ModelSerializer):
   class Meta:
        model = Pedido
        fields = ('__all__')


class PlatosSerializers(serializers.ModelSerializer):
   class Meta:
        model = Platos
        fields = ('__all__')

class   ClienteSerializers(serializers.ModelSerializer):
   class Meta:
        model = Cliente
        fields = ('__all__')

class MeseroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mesero
        fields = ('__all__')