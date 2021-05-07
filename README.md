# Djnago Rest Framework

## 목차
- Installation
  - requirement
  - settings
- FBV
  
- CBV

- APIView
  
- Serializer
    - Serializer
    - ModelSerializer
- DjangoORM
    - Model
  
## Installation

### requirement
```bash
$ pip install -r requirements.txt
```
### settings

#### 1.app 만들기
```bash
$ django-admin startapp api
```
#### 2.app 등록
```python
# ...another things
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
]
# ...another things
```
settings.py에 `startapp`을 통해 생성한 `app`과 `rest_framework` 등록

#### 3.DATABASES Config

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_name',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

#### 4. dotenv 설정

```bash
$ pip install django-environ 
```
**`django-environ`**을 이용하여 `.env`파일을 생성하여 설정 값을 보관할 수 있도록 합니다. `.env`의 파일 위치는 settings.py와 같은 위치에 생성합니다.

**(ex - Board_DRF/boardDRF/.env)**

**[.env]**
```dotenv
DEBUG=on
SECRET_KEY=YOUR-SECRETKEY
DATABASE_URL=mysql://username:password@localhost:3306/db_name
```

`environ` 의 DB 혹은 DB_Cache 정보는 [여기](https://github.com/joke2k/django-environ) 서 확인 할 수 있습니다

**[boardDRF/settings.py]**
```python
import environ

env = environ.Env()
env.read_env()

...

SECRET_KEY=env('SECRET_KEY')

...

DATABASES = {
    'default': env.db()
}
```

## FBV

## CBV

## APIView

### GenericAPIView

### ViewSet

## Serializer
**`serializer`** 은 `Model` 로 부터 뽑은 queryset을 JSON형태로 변경하는 클래스 이다. 반대로 
`request` 로 부터 들어온 `Json`형식의 데이터를 validate 후 저장 혹은 Update 를 지정 할 수 있다.

### Serializer

### ModelSerializer

아래는 회원가입을 위한 `Serializer`이다.

```python
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator


class RegisterUserSerializer(serializers.ModelSerializer):
    # validate 기준
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)
    confirm_password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'confirm_password',)
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "password does not matches"})
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        validated_data.pop('confirm_password', None)
        print(validated_data)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
```
#### declare fields
가장 위의 선언부는 Json 형식으로 들어온 request 데이터를 validate 하는 기준을 명시한다.

#### Meta Class
`Meta` 클래스는 대표적으로 아래와 같은 정보를 명시한다.
- model : 삽입 혹은 참조 할 모델명
- fields : `(삽입시)Json 으로 받을 필드명` 혹은 `(조회시)DataBase 에서 조회 할 필드명`
- extra_kwargs : 추가 옵션 (extra_kwargs 에 관하여는 추후에 상세히 더 쓰겠음)

```python
class Meta:
        model = CustomUser # 모델명
        fields = ('email', 'username', 'password', 'confirm_password',) # request 로 부터 전달 받을 필드
        extra_kwargs = {'password': {'write_only': True}} # 추가 옵션
```

추가적으로 model의 모든 필드를 field에 명시하고 싶을 경우에는 아래와 같이 필드를 선언 할 수 있다.

```python
class Meta:
    model = CustomUser # 모델명
    fields = '__all__'
```

명시한 필드를 제외한 나머지 필드를 명시 하고 싶을 경우에는 `fields` 대신 `exclude` 를 사용 할 수 있다.

```python
class Meta:
    model = CustomUser # 모델명
    exclude = ('username', ) # 제외할 column 명
```



## DjangoORM

### Model

### Simple JWT
