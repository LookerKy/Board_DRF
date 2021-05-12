from django.contrib import admin
from .models import BoardModel, PostModel, TopicModel


# Register your models here.
@admin.register(BoardModel, PostModel, TopicModel)
class AdminBoard(admin.ModelAdmin):
    pass
