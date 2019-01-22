import sys
sys.stdin=open('sample4_input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    R = list(map(int, input().split()))
    result = []                         # 결과값
    ans = ''
    # 리스트 정렬
    for i in range(0, len(R)-1):
        min = i
        for j in range(i+1, len(R)):
            if R[min] > R[j]:
                min = j
        R[i], R[min] = R[min], R[i]
    # 큰값은 마지막, 작은 값은 처음 조건
    while R:
        result.append(R.pop(-1))
        result.append(R.pop(0))
        if len(result) == 10:           # 특별히 정렬된 숫자 10개 조건
            break

    # for i in range(len(result)):
    #     result[i] = str(result[i])
    # ans = ' '.join(result)

    print(f'#{test_case + 1} {" ".join(map(str, result))}')