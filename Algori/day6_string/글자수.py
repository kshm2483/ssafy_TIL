import sys
sys.stdin = open('글자수_input.txt', 'r')
T = int(input())

for tc in range(T):
    str1 = input()
    str2 = input()
    max = -1                # 최대값 저장

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:      # 같은 글자이면 카운트
                cnt += 1
        if cnt > max:       # 카운트가 제일 높은 글자로 변환
            max = cnt

    print(f'#{tc+1} {max}')