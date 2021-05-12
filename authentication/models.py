from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from .utils import Gender


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, gender=Gender.Male, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, gender=gender, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        pass

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        pass


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

    objects = CustomUserManager()

    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
