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
#### app 만들기
```bash
$ django-admin startapp board
```
#### app 등록
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
`startapp`을 통해 생성한 app과 `rest_framework` 등록

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
