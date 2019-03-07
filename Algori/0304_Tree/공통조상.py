def findp(node):
    if tree[node][2] == 0:
        result.append(node)
        return
    findp(tree[node][2])
    result.append(node)

def preorder(node):
    global cnt
    if node != 0:
        cnt += 1
        preorder(tree[node][0])
        preorder(tree[node][1])

import sys
sys.stdin = open('공통조상_input.txt', 'r')

for tc in range(int(input())):
    V, E, S, G = map(int, input().split())
    temp = list(map(int, input().split()))

    tree = [[0]*3 for _ in range(V+1)]

    result = []
    cnt = 0
    for i in range(len(temp)):
        if i%2 == 1:
            tree[temp[i]][2] = temp[i-1]
        else:
            if tree[temp[i]][0] == 0:
                tree[temp[i]][0] = temp[i+1]
            else:
                tree[temp[i]][1] = temp[i+1]

    findp(S)
    findp(G)

    a = []

    for i in result:
        if result.count(i) > 1 and i not in a:
            a.append(i)

    preorder(a[-1])
    print('#{} {} {}'.format(tc+1, a[-1], cnt))