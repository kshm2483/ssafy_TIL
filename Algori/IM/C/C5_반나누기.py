import sys
sys.stdin = open('C5_반나누기_input.txt', 'r')

for tc in range(int(input())):
    N, KMn, KMx = map(int, input().split())
    score = list(map(int, input().split()))

    result = []

    for T1 in range(1, 101):
        for T2 in range(T1+1, 101):
            A = []
            B = []
            C = []

            for i in score:
                if i >= T2:
                    A.append(i)
                elif i < T1:
                    C.append(i)
                else:
                    B.append(i)

            leng = [len(A), len(B), len(C)]

            if max(leng) <= KMx and min(leng) >= KMn:
                ans = max(leng) - min(leng)
                result.append(ans)
    if result:
        print(ans)
    else:
        print(-1)