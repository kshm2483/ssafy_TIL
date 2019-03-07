# 13 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

V, E = map(int, input().split())
num = list(map(int, input().split()))

data = [[0]*3 for _ in range(V+1)]

for i in range(len(num)):
    if i%2 == 1:
        data[num[i]][2] = num[i-1]
    else:
        if data[num[i]][0] == 0:
            data[num[i]][0] = num[i+1]
        else:
            data[num[i]][1] = num[i+1]

for i in range(1, V+1):
    print('{:2} {:2} {:2} {:2}'.format(i, data[i][0], data[i][1], data[i][2]))


def preorder(node):
    if node != 0:
        print('{}'.format(node), end=' ')
        preorder(data[node][0])
        preorder(data[node][1])

def inorder(node):
    if node != 0:
        inorder(data[node][0])
        print('{}'.format(node), end=' ')
        inorder(data[node][1])

def postorder(node):
    if node != 0:
        postorder(data[node][0])
        postorder(data[node][1])
        print('{}'.format(node), end=' ')

preorder(1)
print()
inorder(1)
print()
postorder(1)