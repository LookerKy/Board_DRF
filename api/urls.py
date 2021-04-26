from django.urls import path, include
from .views import hello_api

urlpatterns =[
    path('hello/', hello_api)
]
