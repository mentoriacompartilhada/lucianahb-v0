from .models import Pessoas
from rest_framework import serializers

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoas
        fields = '__all__'
        # fields = '__all__' é igual a exlude = [],
        # mas só posso usar 1 ou outro
