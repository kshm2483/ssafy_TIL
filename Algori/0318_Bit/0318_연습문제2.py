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

def xtoo(x):
    if x <= '9':
        return ord(x) - ord('0')
    else:
        return ord(x) - ord('A') + 10

def otob(x):
    global B
    for i in range(4):
        B.append(asc[x][i])

A = '0F97A3'
# 0000 1111 1001 0111 1010 0011
B = []

for i in range(len(A)):
    otob(xtoo(A[i]))

n = 0
for i in range(len(B)):
    n = n * 2 + B[i]
    if i % 7 == 6:
        print(n, end=', ')
        n = 0

if i % 7 != 6:
    print(n)