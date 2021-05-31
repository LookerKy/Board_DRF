from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from .serializer import BoardSerializer, TopicListSerializer, TopicSerializer
from .models import BoardModel, TopicModel


class BoardList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BoardModel.objects.all()
    serializer_class = BoardSerializer


class TopicList(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BoardModel.objects.all()
    serializer_class = TopicListSerializer


# Topic List만 나오게
class TopicLists(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        queryset = get_object_or_404()



