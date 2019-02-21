# 190220_CRUD/C9

## 1.create

### 1.0 설계도 작성

```bash
python manage.py makemigrations boards
# 아무것도 변화시키지 않고 확인만 할때 사용
python manage.py sqlmigrate boards 0001
```

### 1.1 디비작성

디비를 만들자

```bash
python manage.py migrate
```

```bash
# c9 인터프리터 실행
python manage.py shell
# python 코드 작성
from boards.models import Board
Board.objects.all()					# <QuerySet []> 빈 쿼리셋 리턴
# 새로운 객체생성
board = Board()
board.title = 'first'
board.content = 'django!'
board.save()						# 저장
```

### 1.2 django extensions

```bash
pip install django-extensions
```
> settings.py에 INSTALLED_APPS에 extensions 추가이후 사용

```bash
# 모델들을 import 해옴
python manage.py shell_plus
```

```bash
# 디비작성 줄임판 1
board = Board(title='second', content='django!!')
board.save()
Board.objects.all()
```

```bash
# 디비작성 줄임판 2
# save까지 실행
Board.objects.create(title='thirds', content='django!!!')
```

### 1.3 예외처리

```bash
# django orm 검증
board.full_clean()
```

## 2.READ

### 2.1 검색

```bash
# 몇 개인지 모르기때문에 리스트로 반환 / 정확한 선택이 힘듦
Board.objects.filter(title='first').all()
>>> <QuerySet [<Board: 1: first>]>
# 한개만 반환
Board.objects.filter(title='first').first()
>>> <Board: 1: first>
# 없는거 검색
Board.objects.filter(title='missing').first()
>>> return None									# 아무것도 안뜲
```

> id 검색

```bash
# primary_key 검색
board = Board.objects.get(pk=1)
# filter로 가져오면 리스트로 반환하기 때문에 id는 필터로 접근하면 안된다
board = Board.objects.filter(id=1)
```

### 2.2 Like

```bash
# 포함
boards = Board.objects.filter(title__contains='fi').all()
# 시작
boards = Board.objects.filter(title__startswith='fi').all()
# 끝
boards = Board.objects.filter(content__endswith='!')
```

### 2.3 정렬

```bash
# - 를 붙이면 역방향 정렬
boards = Board.objects.order_by('-title').all()
```

## 3.update

```bash
board = Board.objects.get(pk=1)
board.title = 'hello'
board.save()
board.title
```

## 4.delete

```bash
board.delete()
```

