import sys
sys.stdin = open('0319_이진수2.txt')

for tc in range(int(input())):
    N = float(input())

    cnt = 0
    ans = ''
    while cnt < 13:
        cnt += 1
        if N == 0:
            break
        if N * 2 >= 1:
            ans += '1'
            N = N * 2 - 1
        else:
            ans += '0'
            N = N * 2
    if len(ans) < 13:
        print('#{} {}'.format(tc+1, ans))
    else:
        print('#{} overflow'.format(tc+1))