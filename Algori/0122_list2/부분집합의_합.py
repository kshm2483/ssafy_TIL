import sys
sys.stdin=open('sample2_input.txt', 'r')

T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())    # 원소의 수 N, 부분 집합의 합 K
    A = list(range(1, 13))              # 1 ~ 12 리스트
    cnt = 0                             # 부분집합의 개수
    for i in range(1 << len(A)):
        ziphap = []                     # 조건을 판단하기 위한 리스트 / 매번 초기화
        for j in range(len(A)):
            if i & (1 << j):
                ziphap.append(A[j])
        if len(ziphap) == N and sum(ziphap) == K:
            cnt += 1                    # 두 조건을 만족해야 카운트

    print(f'#{test_case + 1} {cnt}')