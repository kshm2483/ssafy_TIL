## ORM (Object-relational mapping)

>  객체형 데이터와 관계형 데이터의 각 속성들을 매핑할 경우, 관계형 데이터를 객체형 데이터처럼 사용가능하다. 쉽게 말해, SQL문 작성 없이 간단한 매핑설정으로 데이터 베이스의 테이블 데이터를 객체로 전달 받을 수 있는 것이다.

#### ORM의 장점

1. 생산성 / 유지보수성 향상
2. 독립성

#### 환경설정

```python
pip install flask_sqlalchemy
pip install flask_migrate
```

  >  app.py, models.py 파일 생성 후

```python
flask db init
// migrations 파일 생성
flask db migrate
// sqlite3 파일 생성
flask db upgrade
```
#### 사용방법 ( SQL to ORM)

 > ORM READ

```sqlite
SELECT * FROM users;
```
```python
users = User.query.all()
```

>ORM INSERT

```sqlite
INSERT INTO users(username, email)
VALUES ('jin', 'example@gmail.com')
```

```python
from app import *
user = User(username='jin', email='example@gmail.com')
db.session.add(user)
db.session.commit()
```
> ORM SELECT

```sqlite
SELECT * FROM users WHERE username='jin'
```

```python
user = User.query.filter_by(username='jin').all()
```

| SQL     | SQLAlchemy |
| ------- | ---------- |
| LIMIT 1 | .first()   |

> Get one by id / PK만 get으로 가져올 수 있음

```sqlite
SELECT * FROM users WHERE id=1;
```

```python
user = User.query.get(1)
```
>LIKE
```python
users = User.query.filter(User.email.like('%exam%')).all()
users = User.query.limit(1).offeset(2).all()
```
> UPDATE

```python
user = User.query.get(1)
db.session.commit()
user.username
```
> DELETE

```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

