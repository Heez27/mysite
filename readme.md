# mysite01 장고 프로젝트 만들기

### 1. django library 설치
```shell
(env) # pip install django
```

### 2. mysqlclient library 설치 (ORM 적용할 경우, 생략)
```shell
(env) # pip install mysqlclient
```

### 3. 장고 프로젝트 생성
```shell
(env) # django-admin startproject mysite
```

### 4. 디렉토리 정리(pycharm 프로젝트와 장고 프로젝트를 일치시켜 주기)

### 5. 초기 설정(settings.py)
1) time zone 설정
```python
TIME_ZONE = 'Asia/Seoul'
```   
2) database 설정
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webdb',
        'USER': 'webdb',
        'PASSWORD': 'webdb',
        'HOST': 'localhost',
        'PORT': 3306
    }
}
```

3) DATETIME Format 설정(생략)
```python
DATETIME_FORMAT = "Y-m-d P h:i:s"
L10N = False
USE_TZ = False
```
### 6. admin 애플리케이션 삭제하기(settings.py, urls.py)
1) INSTALLED_APPS = [ ... ] 에서 'django.contrib.admin' 삭제
2)urlpatterns = [] 에서 'admin/' 매핑 삭제
   

### 7. ORM을 적용하고 mysql5.1x 인 경우 manage.py 수정
```python
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime'
```

### 8. Application들의 통합 template 디렉토리 templates 만들기
1) 디렉토리 생성
    mysite01
       |--- templates

2) template 디렉토리 설정(settings.py)
```python
import os

'DIRS': [os.path.join(BASE_DIR, 'templates')]
```

### 9. static 파일(css, js, images) 설정(settings.py)

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'statics'),
)
STATIC_URL = '/assets/'
```

### 10. 지금까지 작업 내용 확인

1) 서버 시작하기
```shell
(env) # python manage.py runserver 0.0.0.0:9999
```


2) 브라우저로 접근하기: url http://localhost:9999 로 접근