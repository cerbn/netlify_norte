# api/serializers.py

from rest_framework import serializers
from .models import OrdenDespacho

class OrdenDespachoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenDespacho
        fields = '__all__'
