from django.urls import path
from .views import BoardList

urlpatterns = [
    path('boards/', BoardList.as_view(), name="board_list")
]
