import sys
sys.stdin = open('C6_도넛츠합계_input.txt', 'r')

N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

def donut(x, y):
    global maxh
    hap = 0
    minu = 0
    for i in range(K):
        for j in range(K):
            hap += data[x+i][y+j]
    for i in range(x+1, x+2):
        for j in range(y+1, y+2):
            minu += data[i][j]

    return hap-minu

maxh = 0
for i in range((N-K)+1):
    for j in range((N-K)+1):
        a = donut(i, j)
        if a > maxh:
            maxh = a

print(maxh)