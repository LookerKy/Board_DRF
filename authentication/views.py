from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import permissions, status
from .serializer import UserTokenSerializer, CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view


class UserTokenView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(serializer)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        print(serializer.validated_data["refresh"])

        # @TODO get Device setCookie Or Just Json
        response = JsonResponse({"access": serializer.validated_data["access"]}, status=status.HTTP_200_OK)
        response.set_cookie('refresh', serializer.validated_data["refresh"], httponly=True)
        return response


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
