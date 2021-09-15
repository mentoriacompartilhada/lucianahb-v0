# from django.shortcuts import render
from django.db.models import query
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client


def hello_world(request):
    return HttpResponse("Hello World")


class ClientViewSet (viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer

# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

# class ClientListView(ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class ClientCreateView(CreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class ClientUpdateView(UpdateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class ClientRetrieveView(RetrieveAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# class ClientDestroyView(DestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer


# client = ClientListView.as_view()
# client = ClientCreateView.as_view()
# client = ClientUpdateView.as_view()
# client = ClientRetrieveView.as_view()
# client = ClientDestroyView.as_view()
