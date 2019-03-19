import sys
sys.stdin = open('0319_이진수.txt')

asc = [[0,0,0,0],  # 0
       [0,0,0,1],  # 1
       [0,0,1,0],  # 2
       [0,0,1,1],  # 3
       [0,1,0,0],  # 4
       [0,1,0,1],  # 5
       [0,1,1,0],  # 6
       [0,1,1,1],  # 7
       [1,0,0,0],  # 8
       [1,0,0,1],  # 9
       [1,0,1,0],  # A
       [1,0,1,1],  # B
       [1,1,0,0],  # C
       [1,1,0,1],  # D
       [1,1,1,0],  # E
       [1,1,1,1],] # F
# 0100 0111 1111 1110
def xtoo(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('A') + 10

def otob(x):
    global ans
    for i in range(4):
        ans += str(asc[x][i])

for tc in range(int(input())):
    N, M = map(str, input().split())
    ans = ''
    for i in M:
        otob(xtoo(i))
    print('#{} {}'.format(tc+1, ans))