ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}
# semester1 기간 출력
print(ssafy["duration"]["semester1"])
# 딕셔너리 안에 있는 대전출력 index값
print(ssafy["location"][1])
# 대전 매니저 이름 출력
print(ssafy["classes"]["daejeon"]["manager"])