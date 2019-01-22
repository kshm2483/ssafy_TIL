import sys
sys.stdin=open('sample1_input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    arr= [[0 for _ in range(10)] for _ in range(10)]
    cnt = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for y in range(r1, r2+1):               # 행의 방향
            for x in range(c1, c2+1):           # 열의 방향
                arr[x][y] += color              # 행렬에 color 추가
                # 겹쳐지는 부분 카운트
                if arr[x][y] == 3:
                    cnt += 1

    print(f'#{test_case + 1} {cnt}')