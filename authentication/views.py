from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import permissions, status
from .serializer import UserTokenSerializer, RegisterUserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from .models import CustomUser


# @ TODO create Android token API


class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def get(self, request):
        if request.COOKIES:
            print(request.COOKIES['refresh'])
            serializer = self.get_serializer(data={'refresh': request.COOKIES['refresh']})
            try:
                serializer.is_valid(raise_exception=True)
                print(serializer.validated_data)
            except TokenError as e:
                raise InvalidToken(e.args[0])
            response = JsonResponse({"access": serializer.validated_data["access"]}, status=status.HTTP_200_OK)
            response.set_cookie('refresh', serializer.validated_data["refresh"], httponly=True)
            return response
        else:
            return Response({"message": "failure"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        return Response({"message": "failure"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(serializer)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # print(serializer.validated_data["refresh"])
        # Response(serializer.validated_data, status=status.HTTP_200_OK)
        response = JsonResponse({"access": serializer.validated_data["access"]}, status=status.HTTP_200_OK)
        response.set_cookie('refresh', serializer.validated_data["refresh"], httponly=True)
        return response


# @TODO APIView to GenericAPIView 로 변경
class CustomUserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)


class UserRegisterView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


@api_view(['GET'])
def user_profile(request):
    user = CustomUser.objects.get(email=request.user.email)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
