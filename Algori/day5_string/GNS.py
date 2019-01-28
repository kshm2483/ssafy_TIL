import sys
sys.stdin = open('GNS_test_input.txt', 'r')
T=int(input())

for tc in range(T):
    temp=input() # dummy
    data=list(map(str, input().split()))
    # 각 숫자를 카운트할 딕셔너리 생성
    cnt = {'ZRO':0, 'ONE':0, 'TWO':0, 'THR':0, 'FOR':0,
           'FIV':0, 'SIX':0, 'SVN':0, 'EGT':0, 'NIN':0}
    # data를 돌면서 카운팅
    for i in range(len(data)):
        cnt[data[i]] += 1
    # 테스트 케이스 출력
    print(f'#{tc+1}')
    # key를 value만큼 출력
    for key, value in cnt.items():
        print((key+' ')*value, end='')
    # 개행
    print()