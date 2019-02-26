def find(s):
    global visited, G
    if s == G:
        return 0

    Q = []
    Q.append(s)
    visited[s] = 1
    while Q:
        s = Q.pop(0)
        for i in range(V+1):
            if temp[s][i] == 1 and visited[i] == 0:
                Q.append(i)
                visited[i] = visited[s] + 1
    if visited[G] == 0:
        return 0
    else:
        return visited[G] - 1

import sys
sys.stdin = open('노드의_거리_input.txt', 'r')

for tc in range(int(input())):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())

    # 노드입력
    temp = [[0]*(V+1) for _ in range(V+1)]

    for i in data:
        temp[i[0]][i[1]] = 1
        temp[i[1]][i[0]] = 1
    # 방문
    visited = [0]*(V+1)



    print(f'#{tc+1} {find(S)}')