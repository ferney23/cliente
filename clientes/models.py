from django.db import models
class Cliente(models.Model):
    id_Cliente = models.IntegerField(unique=True, primary_key=True)


class Platos(models.Model):
    id_plato = models.IntegerField(unique=True, primary_key=True)
    precio = models.IntegerField(null=False, blank=True)
    calificacion_plato = models.IntegerField(null=True, blank=True)
    pedido = models.ForeignKey('clientes.Pedido', on_delete=models.CASCADE, null=True, blank=True)
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, null=True, blank=True)
    menu=models.ForeignKey('clientes.Menu', on_delete=models.CASCADE, null=True, blank=True)
    factura=models.ForeignKey('clientes.Factura', on_delete=models.CASCADE, null=True, blank=True)



class Mesa(models.Model):
    id_mesa = models.IntegerField(unique=True, primary_key=True)
    estado_mesa = models.BooleanField(default=True,null=False, blank=True)

class Menu(models.Model):
    id_menu = models.IntegerField(unique=True, primary_key=True)

class Pedido(models.Model):
    id_pedido = models.IntegerField(unique=True, primary_key=True)


class Factura(models.Model):
    id_factura = models.IntegerField(unique=True, primary_key=True)
    mesero = models.ForeignKey('clientes.Mesero', on_delete=models.CASCADE, null=True, blank=True)
    cliente =models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE, null=True, blank=True)


class Mesero(models.Model):
    id_mesero = models.IntegerField(unique=True, primary_key=True)
    calificacion_mesero= models.IntegerField(null=False, blank=True)

