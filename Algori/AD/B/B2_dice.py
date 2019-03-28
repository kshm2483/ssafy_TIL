import sys
sys.stdin = open('B2_dice.txt')

def DFS(sums, cnt):
    if sums > M: return
    if cnt == N:
        if sums == M:
            print(*dice)
        return
    for i in range(1, 7):
        dice[cnt] = i
        DFS(sums+i, cnt+1)


N, M = map(int, input().split())

sums = 0
cnt = 0
dice = [0]*N

DFS(sums, 0)