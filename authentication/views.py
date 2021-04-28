from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions
from .serializer import UserTokenSerializer


class UserTokenView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserTokenSerializer


