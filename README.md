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
    'knox',
]
# ...another things
```
settings.py에 `startapp`을 통해 생성한 app과 `rest_framework`, `django-rest-knox` 등록

#### 3.DATABASES Config

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'k_board',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## FBV

## CBV

## APIView

### GenericAPIView

### ViewSet

## Serializer

### Serializer

### ModelSerializer

## DjangoORM

### Model
