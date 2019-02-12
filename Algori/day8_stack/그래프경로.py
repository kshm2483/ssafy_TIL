import sys
sys.stdin = open('그래프경로_input.txt', 'r')

T = int(input())

def graph(data, start, goal):
    global flag
    if start == goal:
        flag = 1
        return
    visit[start] = 1
    for i in range(V+1):
        if data[start][i] == 1 and visit[i] == 0:
            graph(data, i, goal)

for tc in range(T):
    flag = 0
    V, E = map(int, input().split())
    data = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        data[a][b] = 1
    S, G = map(int, input().split())
    visit = [0 for i in range(V+1)]
    graph(data, S, G)
    print(f'#{tc+1} {flag}')