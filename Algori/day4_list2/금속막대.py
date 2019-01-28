import sys
sys.stdin=open('input.txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    nasa = list(map(int, input().split()))
    new_nasa = []
    # 겹치지지 않는 시작값
    for i in range(len(nasa)):
        if i%2 == 0 and nasa.count(nasa[i]) == 1:
            new_nasa.append(nasa[i])
            new_nasa.append(nasa[i+1])
    # 뒤에 오는값 더하기
    while len(nasa) != len(new_nasa):
        for i in range(len(nasa)):
            if i%2 == 0 and nasa[i] == new_nasa[-1]:
                new_nasa.append(nasa[i])
                new_nasa.append(nasa[i+1])
    print(f'#{test_case + 1} {" ".join(map(str, new_nasa))}')