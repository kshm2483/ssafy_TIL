import sys
sys.stdin = open('B4_minsum.txt')

def DFS(n, sums):
    global mins
    if sums > mins:
        return
    if n == N:
        if mins > sums:
            mins = sums
        return

    for i in range(len(data[n])):
        if chk[i]: continue
        chk[i] = 1
        DFS(n+1, sums + data[n][i])
        chk[i] = 0

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
chk = [0]*N
mins = 0xfffffff
summ = 0

DFS(0, 0)

for i in range(N):
    summ += min(data[i])
print(summ)
print(mins)