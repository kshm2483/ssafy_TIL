import sys
sys.stdin=open('sample3_input.txt', 'r')

T = int(input())

for test_case in range(T):
    P, Pa, Pb = map(int, input().split())

    find = {'Pa': 0, 'Pb': 0}       # 카운트를 저장할 장소
    read_cnt1, read_cnt2 = 0, 0     # 카운트
    start1, start2 = 1, 1           # 시작 페이지 설정
    winner = 0
    end = P                         # 2번째 카운트할 페이지 저장
    # A의 페이지 찾기
    while find['Pa'] == 0:
        read_cnt1 += 1
        middle = (start1 + P)//2
        if middle == Pa:
            find['Pa'] = read_cnt1
        elif middle > Pa: P = middle
        else: start1 = middle
    # B의 페이지 찾기
    while find['Pb'] == 0:
        read_cnt2 += 1
        middle = (start2 + end)//2
        if middle == Pb:
            find['Pb'] = read_cnt2
        elif middle > Pb: end = middle
        else: start2 = middle
    # 승자 찾기
    if find['Pa'] > find['Pb']:
        winner = 'B'
    elif find['Pa'] < find['Pb']:
        winner = 'A'

    print(f'#{test_case + 1} {winner}')