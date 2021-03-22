
from rest_framework import serializers
from .models import Gateau

class GatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateau
        fields = '__all__'