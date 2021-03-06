from rest_framework import serializers
from .models import BoardModel


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = '__all__'
