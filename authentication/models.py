from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from enum import Enum


class Gender(Enum):
    male = 'Male'
    female = 'Female'


class CustomUser(AbstractUser):
    username_validator = UnicodeUsernameValidator

    first_name = None
    last_name = None
    gender = models.CharField(max_length=6, choices=[(tag, tag.value) for tag in Gender])

    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
