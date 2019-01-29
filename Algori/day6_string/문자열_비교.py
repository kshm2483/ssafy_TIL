import sys
sys.stdin = open('문자열_비교_input.txt', 'r')
T = int(input())

for test_case in range(T):
    pattern = input()
    string = input()
    N = len(pattern)
    M = len(string)
    i, j = 0, 0
    result = 0
    while i < N and j < M:              # bruteforce
        if pattern[i] != string[j]:
            j = j - i
            i = -1                      # 문자열이 다르면 복구
        j = j + 1
        i = i + 1
    if i == N:
        result += 1

    print(f'#{test_case+1} {result}')