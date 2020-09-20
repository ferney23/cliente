import os

import random

from rest_framework import viewsets, status
from rest_framework.decorators import action

from .models import (Menu,Factura,Mesa,Pedido,Platos,Cliente,Mesero)
from .serializers import (ClienteSerializers,FacturaSerializers,MenuSerializers,
                          PedidoSerializers,MesaSerializers,PlatosSerializers,MeseroSerializers)

from rest_framework.response import Response

"""
THREADS_COUNT = 1

class Threaded_worker(threading.Thread):
    def __init__(self, sleep_time):
        threading.Thread.__init__(self)
        self.sleep_time = sleep_time
    def run(self):
        threadName = threading.currentThread().getName()
        print("[%s] Hello, I am %s and I will sleep %d seconds." % (datetime.now().strftime('%H:%M:%S'), threadName, self.sleep_time))
        time.sleep(self.sleep_time)
        print("[%s] I am %s and I have waken up." % (datetime.now().strftime('%H:%M:%S'), threadName))


"""

class ClientesViewsets(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializers




"""
    def imprimir2(self,n):
        while (True):
            print('{0} imprime2 {1}\n'.format(threading.current_thread().name, n), end='')
            time.sleep(0)


    @action(methods=['get'], detail=False)
    def mac(self, request, pk=None):

        for i in range(1):
            hilo = threading.Thread(name='Hilo{}'.format(i), target=self.imprimir, args=(1,))
            hilo.start()

        return Response(status=status.HTTP_200_OK)

"""
"""
    @action(methods=['get'], detail=False)
    def mac(self, request, pk=None):
        print(THREADS_COUNT)

        for i in range(THREADS_COUNT):
            #sleep_time = random.randint(1, 10)
            td = Threaded_worker(10)
            td.start()
        return Response(status=status.HTTP_200_OK)
"""

"""
    def worker(self,pk):
       
        personas=Cliente.objects.filter(pk=pk)
        print(pk)
        print(personas)
        return

    @action(methods=['get'], detail=True )
    def mac(self, request, pk=None):
        threads = list()
        for i in range(3):
            t = threading.Thread(target=self.worker,args=(pk,))
            threads.append(t)
            t.start()
        return Response({'pk':pk},status=status.HTTP_200_OK)
 """


class FacturasViewsets(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializers

    @action(methods=['get'], detail=True)
    def pedido(self, request, pk=None):
        try:
            queryset = Factura.objects.filter(mesero=pk)
            serializer_class = FacturaSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def cliente(self, request, pk=None):
        try:
            queryset = Factura.objects.filter(cliente=pk)
            serializer_class = FacturaSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MesaViewsets(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializers


    @action(methods=['get'], detail=False)
    def ocupadas(self, request, pk=None):
        try:
            queryset = Mesa.objects.filter(estado_mesa=False)
            serializer_class = MesaSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=False)
    def vacias(self, request, pk=None):
        try:
            queryset = Mesa.objects.filter(estado_mesa=True)
            serializer_class = MesaSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PedidoViewsets(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers

class MenuViewsets(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializers

class PLatoViewsets(viewsets.ModelViewSet):
    queryset = Platos.objects.all()
    serializer_class = PlatosSerializers

    @action(methods=['get'], detail=True)
    def pedido(self, request, pk=None):
        try:
            queryset = Platos.objects.filter(pedido=pk)
            serializer_class = PlatosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def cliente(self, request, pk=None):
        try:
            queryset = Platos.objects.filter(cliente=pk)
            serializer_class = PlatosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def menu(self, request, pk=None):
        try:
            queryset = Platos.objects.filter(menu=pk)
            serializer_class = PlatosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def factura(self, request, pk=None):
        try:
            queryset = Platos.objects.filter(factura=pk)
            serializer_class = PlatosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class MeseroViewsets(viewsets.ModelViewSet):
    queryset = Mesero.objects.all()
    serializer_class = MeseroSerializers
