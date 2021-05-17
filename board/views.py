from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import permissions
from .serializer import BoardSerializer
from .models import BoardModel


class BoardList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = BoardModel.objects.all()
    serializer_class = BoardSerializer
