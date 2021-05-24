from django.urls import path
from .views import BoardList, TopicList

urlpatterns = [
    path('boards/', BoardList.as_view(), name="board_list"),
    path('boards/<int:pk>/', TopicList.as_view(), name='topic_list')
]
