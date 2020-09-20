from django.contrib import admin

# Register your models here.
from .models import (Factura,Cliente,Platos,Menu,Pedido,Mesero,Mesa)
admin.site.register(Factura)
admin.site.register(Cliente)
admin.site.register(Platos)
admin.site.register(Menu)
admin.site.register(Pedido)
admin.site.register(Mesero)
admin.site.register(Mesa)