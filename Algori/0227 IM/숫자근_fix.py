def calc(num):
    while True:
        temp = list(map(int, str(num)))
        tot = sum(temp)
        if tot < 10: return tot
        num = tot