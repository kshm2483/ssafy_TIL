import sys
sys.stdin = open('회문_input.txt', 'r')
T = int(input())

def palinddata(data, N, M):
    for x in range(N):
        saero = ''              # 세로 문자열
        for y in range(N-M+1):  # 가로 확인 / (행렬길이 - 회문의 길이)만큼 이동하며 반복
            if data[x][y:M+y] == data[x][y:M+y][::-1]:
                return data[x][y:M+y]
        for z in range(N):      # 세로 문자를 저장
            saero += data[z][x]
        for q in range(N-M+1):  # 세로 확인
            if saero[q:M+q] == saero[q:M+q][::-1]:
                return saero[q:M+q]

for tc in range(T):
    N, M = map(int, input().split())    # N은 행렬 / M은 회문의 길이
    data = [input()for _ in range(N)]
    print(f'#{tc + 1} {palinddata(data, N, M)}')