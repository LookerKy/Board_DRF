from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from .serializer import UserTokenSerializer, CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer



class CustomUserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def hello_world(request):
    return Response(data={"hello": "world"}, status=status.HTTP_200_OK)
