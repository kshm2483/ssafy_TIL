import sys
sys.stdin = open('A3_countNum.txt')

def Bns(t, s, e):
    cnt = 0

    while s <= e:
        m = (s + e) // 2
        if N_data[m] == t:
            for i in range(s-1, e+1):
                if N_data[i] == t:
                    cnt += 1
            return cnt
        elif N_data[m] > t:
            e = m - 1
        else:
            s = m + 1

N = int(input())
N_data = list(map(int, input().split()))
M = int(input())
M_data = list(map(int, input().split()))

for t in M_data:
    a = Bns(t, 0, len(N_data)-1)
    if a:
        print(a, end=' ')
    else:
        print(0, end=' ')