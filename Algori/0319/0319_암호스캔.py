import sys
sys.stdin = open('0319_암호스캔.txt')

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

def findp(x, y):
    global nwlist, cipher
    for i in range(10):
        a = len(cipher[i]) - 1
        b = 0
        result = len(cipher[i])
        while len(cipher[i]) > a:
            if int(cipher[i][a]) == data[x][y-b]:
                b += 1
                a -= 1
            else:
                break
        if result == b:
            nwlist.append(i)
            return 7*code
    return 0

def findlength(x, y):
    global code
    a = 0
    while data[x][y-a] != 0:
        a += 1
    b = 0
    while data[x][y-a-b] != 1:
        b += 1
    c = 0
    while data[x][y-a-b-c] != 0:
        c += 1
    code = min(a, b, c)

def makecipher():
    global code, cipher
    patten = { 0:('1'*2*code)+('0'*1*code)+('1'*1*code),
               1:('1'*2*code)+('0'*2*code)+('1'*1*code),
               2:('1'*1*code)+('0'*2*code)+('1'*2*code),
               3:('1'*4*code)+('0'*1*code)+('1'*1*code),
               4:('1'*1*code)+('0'*3*code)+('1'*2*code),
               5:('1'*2*code)+('0'*3*code)+('1'*1*code),
               6:('1'*1*code)+('0'*1*code)+('1'*4*code),
               7:('1'*3*code)+('0'*1*code)+('1'*2*code),
               8:('1'*2*code)+('0'*1*code)+('1'*3*code),
               9:('1'*1*code)+('0'*1*code)+('1'*2*code)}
    cipher = patten

def verify(temp):
    sumod, sumev = 0, 0
    for i in range(len(temp)):
        if i % 2 == 1:
            sumod += temp[i]
        else:
            sumev += temp[i]

    if ((sumod * 3) + sumev) % 10 == 0:
        return sumod + sumev
    else:
        return 0

for tc in range(int(input())):
    N, M = map(int, input().split())
    # 2진수 저장
    data = []
    for i in range(N):
        a = list(map(str, input()))
        b = ''
        for j in range(len(a)):
            if a[j] <= '9':
                b += ''.join(map(str, asc[int(a[j])]))
            else:
                b += ''.join(map(str, asc[ord(a[j]) - ord('A') + 10]))
        data.append(list(map(int, b)))

    # 암호찾기
    ans = []
    reans = 0
    Mp = M*4
    code = 0

    cipher = {}

    for i in range(1, N):
        j = Mp - 2
        while j > 0:
            if data[i][j] == 1:
                if data[i - 1][j] == 0 and data[i][j + 1] == 0:
                    findlength(i, j)
                    makecipher()
                    k = j
                    nwlist = []
                    while k > 0:
                        if len(nwlist) == 8:
                            break
                        a = findp(i, k)
                        if a != 0:
                            k -= 7*code
                        else:
                            k -= 1
                    j -= (7*code) * 8
                    ans.append(nwlist)
                else:
                    j -= 1
            else:
                j -= 1

    for i in range(len(ans)):
        a = verify(ans[i])
        reans += a
    print('#{} {}'.format(tc+1, reans))