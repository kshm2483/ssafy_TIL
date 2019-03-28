def DFS(n):
    if n == N:
        print(*marble)
        return
    for i in range(1, 4):
        if chk[i]: continue
        chk[i] = 1
        marble[n] = i
        DFS(n+1)
        chk[i] = 0

N = 3
chk = [0]*(N+1)
marble = [0]*N
DFS(0)