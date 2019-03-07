c, r = map(int, input().split())
K = int(input())
data = [['0']*c for _ in range(r)]

cntr = r
cntc = c

def line():
    global cntr, cntc
    x, y = r, 0
    num = 0
    while num < c*r :
        # 상
        for i in range(cntr):
            x -= 1
            num += 1
            data[x][y] = num
            if num == K:
                return print(y+1, r-x)
        cntc -= 1
        # 우
        for i in range(cntc):
            y += 1
            num += 1
            data[x][y] = num
            if num == K:
                return print(y+1, r-x)
        cntr -= 1
        # 하
        for i in range(cntr):
            x += 1
            num += 1
            data[x][y] = num
            if num == K:
                return print(y+1, r-x)
        cntc -= 1
        # 좌
        for i in range(cntc):
            y -= 1
            num += 1
            data[x][y] = num
            if num == K:
                return print(y+1, r-x)
        cntr -= 1
    return print(0)

line()