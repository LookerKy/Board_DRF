from django.utils.timezone import now
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework import permissions, status
from .serializer import UserTokenSerializer, RegisterUserSerializer, UserProfileSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import CustomUser
from .response import set_cookie_response
from django.shortcuts import get_object_or_404


# @ TODO create Android token API
class RefreshTokenView(TokenRefreshView):
    serializer_class = TokenRefreshSerializer

    def get(self, request):
        if request.COOKIES:
            print(request.COOKIES['refresh'])
            serializer = self.get_serializer(data={'refresh': request.COOKIES['refresh']})
            try:
                serializer.is_valid(raise_exception=True)
            except TokenError as e:
                raise InvalidToken(e.args[0])

            return set_cookie_response(serializer.validated_data)
        else:
            return Response({"message": "failure"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        return Response({"message": "failure"}, status=status.HTTP_401_UNAUTHORIZED)


class LoginView(TokenObtainPairView):
    serializer_class = UserTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        # print(serializer.validated_data["refresh"])
        # Response(serializer.validated_data, status=status.HTTP_200_OK)
        set_last_login_time(request.data['email'])

        return set_cookie_response(serializer.validated_data)


class CustomUserRegister(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def user_register(request):
    serializer = RegisterUserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        if user:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "failure"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegisterView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny,)

    # Mixin ????????? ????????? ?????? ??????????????? genericView ??? serializer ??? queryset ??? ????????? api ????????? ????????????.
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


@api_view(['GET'])
def user_profile(request):
    user = get_object_or_404(CustomUser, email=request.user.email)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


def set_last_login_time(email):
    user = CustomUser.objects.get(email=email)
    login_datetime = now()
    user.last_login = login_datetime
    user.save()
