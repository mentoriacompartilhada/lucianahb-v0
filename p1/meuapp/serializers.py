from .models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        # fields = '__all__' é igual a exlude = [],
        # mas só posso usar 1 ou outro
