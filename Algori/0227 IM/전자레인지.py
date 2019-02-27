T = int(input())

A = 300
A_cnt = 0

B = 60
B_cnt = 0

C = 10
C_cnt = 0

fail = 0
while T > 0:
    if T >= 300:
        T -= A
        A_cnt += 1
    elif 300 > T >= 60:
        T -=B
        B_cnt += 1
    elif 60 > T >= 10:
        T -= C
        C_cnt += 1
    elif 10 > T:
        fail = -1
        break
if fail == 0:
    print(f'{A_cnt} {B_cnt} {C_cnt}')
else:
    print(-1)