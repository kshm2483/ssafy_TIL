# DTL

### 0 예시

```python
def template_example(request):
    my_list = ['조미유', '해바라기유', '식용유', '올리브유']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    empty_list = []
    return render(request, 'template_example.html',
                {'my_list':my_list, 'my_sentence':my_sentence,
                 'messages':messages, 'empty_list':empty_list
                })
```

---

### 1 반복문

```html
{% for menu in my_list %}
    <p>{{ menu }}</p>
{% endfor%}
```

1.2

```html
{% for menu in my_list %}
    {{ forloop.counter }}
    {% if forloop.first %}
        <p>조미유+고춧가루</p>
    {% else %}
        <p>{{ menu }}</p>
    {% endif %}
{% endfor%}
```

1.3

> 리스트가 비어있으면 조건

```html
{% for user in empty_list %}
    <p>{{ user }}</p>
{% empty %}
    <p>지금 가입한 회원이 없습니다.</p>
{% endfor %}
```

---

### 2 조건문

```html
{% if '조미유' in my_list %}
    <p>조미유</p>
{% endif %}
```

---

3 length filter

```html
{% for message in messages %}
    {% if message|length > 5 %}
        <p>글씨가 너무 길어요.</p>
    {% else %}
        <p>{{ message }}, {{ message|length }}</p>
    {% endif %}
{% endfor %}
```
---

4 lorem ipsum

> 더미데이터 

```html
{% lorem %}

{% lorem 3 w %}

{% lorem 4 w random %}

{% lorem 2 p %}
```

---

5 Filters

```html
<p>{{ my_sentence|truncatewords:3 }}</p>
<p>{{ my_sentence|truncatechars:5 }}</p>
<p>{{ my_sentence|truncatechars:10 }}</p>
```

---

6 글자 관련 filter

