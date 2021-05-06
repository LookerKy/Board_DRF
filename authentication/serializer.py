from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
import re


class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenSerializer, cls).get_token(user)

        # refresh token print
        # print(token)
        return token


class RegisterUserSerializer(serializers.ModelSerializer):
    # validate 기준
    # RegexField 혹은 RegexValidator 은 왜 안될까?
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    # password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'confirm_password',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        regx = re.compile(r'/^[a-zA-Z]*$/')
        print(regx.match(attrs['username']))
        if regx.match(attrs['username']) is None:
            raise serializers.ValidationError({"username": "username only character"})
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "password does not matches"})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data.pop('confirm_password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username',)
