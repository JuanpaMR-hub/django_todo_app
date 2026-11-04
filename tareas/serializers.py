from .models import Tarea
from rest_framework import serializers



class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['titulo','created_at']