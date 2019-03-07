import sys
sys.stdin = open('C7_초콜릿공장_input.txt', 'r')

N = int(input())
Lc = []
Hc = []
for i in range(N):
    L, H = map(str, input().split())
    Lc.append(L)
    Hc.append(H)


def choco(a, b):
    global cnt
    error = 0
    cntc = 0

    # A공장
    for i in range(len(a)):
        if a.count(a[i]) != 1:
            error = 1
        if b.count(a[i]) > 1:
            error = 1
        elif b.count(a[i]) == 1:
            cntc +=1

    # B공장
    for i in range(len(b)):
        if b.count(b[i]) != 1:
            error = 1

    if cntc > 1:
        error = 1

    if error:
        cnt += 1


cnt = 0

for i in range(N):
    choco(Lc[i], Hc[i])
print(cnt)