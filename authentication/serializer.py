import datetime

from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator


# import re


class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(UserTokenSerializer, cls).get_token(user)
        # refresh token print
        print(type(token))
        return token

    # def create(self, validated_data):
    #     print(validated_data)
    #     print(CustomUser.objects.all())
    #     instance = CustomUser(last_login=datetime.timedelta())
    #     return instance


class RegisterUserSerializer(serializers.ModelSerializer):
    # validate 기준(models에 설정하지 않은 validate가 있을 경우 선언하여 사용)
    # RegexField 혹은 RegexValidator model 과 serializer 둘다 작동하지 않는 문제가 있음 -> 해결 javascript 와 다르게 '/'가 들어가면 안됨
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    # password = serializers.CharField(min_length=8, write_only=True)
    username = serializers.RegexField(required=True, regex=r'^[\w.@+-]+\Z')
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'gender', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def validate(self, attrs):
        # regx = re.compile(r'^[a-zA-Z | 가-힣]*$')
        # print(regx.match(attrs['username']))
        # if regx.match(attrs['username']) is None:
        #     raise serializers.ValidationError({"username": "username only character"})
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
        exclude = ('password',)
