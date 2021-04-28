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
    'rest_framework',
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
**`serializer`** 은 `Model` 로 부터 뽑은 queryset을 JSON형태로 변경하는 클래스 이다.


### Serializer

### ModelSerializer

## DjangoORM

### Model

### Simple JWT
