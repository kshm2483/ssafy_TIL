import sys
sys.stdin = open('A2_findNum.txt')

# 재귀
def BnsRe(t, s, e):
    if s > e: return

    m = (s + e) // 2

    if N_data[m] == t:
        return m + 1
    elif N_data[m] > t:
        e = m - 1
    else:
        s = m + 1
    return BnsRe(t, s, e)

# 반복문
def Bns(t, s, e):
    while s <= e:
        m = (s + e) // 2
        if N_data[m] == t:
            return m + 1
        elif N_data[m] > t:
            e = m - 1
        else:
            s = m + 1

N = int(input())
N_data = list(map(int, input().split()))
T = int(input())
T_data = list(map(int, input().split()))

for t in T_data:
    a = Bns(t, 0, len(N_data) - 1)
    if a:
        print(a)
    else:
        print(0)