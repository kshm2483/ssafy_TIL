import sys
sys.stdin = open('B7_plus.txt')

def DFS(n, k, sums):
    global K, flag
    if flag: return
    if sums > K:
        return
    if n == k:
        if sums == K:
            flag = 1
        return
    else:
        chk[k] = 1
        DFS(n, k+1, sums + data[k])
        if flag: return
        chk[k] = 0
        DFS(n, k+1, sums)

for tc in range(int(input())):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    chk = [0]*N
    flag = 0
    DFS(N, 0, 0)

    if flag:
        print('YES')
    else:
        print('NO')