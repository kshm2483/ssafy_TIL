# Django 시작 명령어들..

```python
# 가상환경 구축
# pyenv virtualenv 3.6.7 'name'
pyenv virtualenv 3.6.7 django-venv
# 가상환경 확인
pyenv virtualenvs
# 가상환경 사용선언
# pyenv local 'name'
pyenv local django-venv
# 장고 설치
pip install django
# 프로젝트 생성
# django-admin startproject 'name' dir
django-admin startproject django_intro .

#서버 열기
python manage.py runserver $IP:$PORT
```

```python
# host 설정 / intro파일의 settings
ALLOWED_HOSTS = ['django-intro-kshm2483.c9users.io']
gitignore 설정
# tree
트리보여줌

# python manage.py startapp 'name'
python manage.py startapp home
# app을 만들었으면 intro파일의 settings을 열어서 추가
INSTALLED_APPS = [
    'home.apps.HomeConfig',
]
```

```
home에 view에 추가하고
intro urls파일 열어서 추가 
from home import views
```

