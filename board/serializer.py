from rest_framework import serializers
from .models import BoardModel, TopicModel


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardModel
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = TopicModel
        fields = '__all__'


class TopicListSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, required=False)

    class Meta:
        model = BoardModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    pass