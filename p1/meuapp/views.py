# from django.shortcuts import render
from django.db.models import query
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import PessoasSerializer
from .models import Pessoas


def hello_world(request):
    return HttpResponse("Hello World")


class PessoasViewSet (viewsets.ModelViewSet):
    queryset = Pessoas.objects.all().order_by('name')
    serializer_class = PessoasSerializer

# from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView

# class PessoasListView(ListAPIView):
#     queryset = Pessoas.objects.all()
#     serializer_class = PessoasSerializer


# class PessoasCreateView(CreateAPIView):
#     queryset = Pessoas.objects.all()
#     serializer_class = PessoasSerializer


# class PessoasUpdateView(UpdateAPIView):
#     queryset = Pessoas.objects.all()
#     serializer_class = PessoasSerializer


# class PessoasRetrieveView(RetrieveAPIView):
#     queryset = Pessoas.objects.all()
#     serializer_class = PessoasSerializer


# class PessoasDestroyView(DestroyAPIView):
#     queryset = Pessoas.objects.all()
#     serializer_class = PessoasSerializer


# pessoas = PessoasListView.as_view()
# pessoas = PessoasCreateView.as_view()
# pessoas = PessoasUpdateView.as_view()
# pessoas = PessoasRetrieveView.as_view()
# pessoas = PessoasDestroyView.as_view()
