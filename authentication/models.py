from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import Gender


class CustomUser(AbstractUser):
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=50, unique=True, error_messages={
        'unique': "this email is already exists."
    })
    gender = models.CharField(max_length=6, choices=Gender.choice(), default=Gender.Male)
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
