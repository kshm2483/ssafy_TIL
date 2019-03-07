import sys
sys.stdin = open('C9_비밀금고_input.txt', 'r')

N = int(input())
data = list(map(int, input().split()))

M = N+N-1

go = [[0]*M for _ in range(M)]

for i in range(M):
    print(go[i])


for i in range(M):
    for j in range(M):
