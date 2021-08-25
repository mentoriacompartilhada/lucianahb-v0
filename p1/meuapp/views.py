# from django.shortcuts import render
# from django.http import HttpResponse

# def hello_world(request):
#     return HttpResponse("Hello World")

from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client


class ClientViewSet (viewsets.ModelViewSet):
    queryset = Client.objects.all().order_by('name')
    serializer_class = ClientSerializer
