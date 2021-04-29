from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserTokenView, CustomUserRegister, hello_world, RefreshTokenView

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('user/create/', CustomUserRegister.as_view(), name='create_user'),
    path('token/obtain/', UserTokenView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('refresh/test/', RefreshTokenView.as_view(), name='test_refresh')
]
