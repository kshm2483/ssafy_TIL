import sys
sys.stdin = open('회문2_input.txt', 'r')

def palind2(data):
    max = -1
    for x in range(100):
        saero = ''
        M, N = 100, 100
        while M > 0:
            for y in range(100-M+1):
                if data[x][y:M + y] == data[x][y:M + y][::-1]:
                    if M > max:
                        max = M
            M -= 1
        for z in range(100):
            saero += data[z][x]
        while N > 0:
            for q in range(100-N + 1):
                if saero[q:N + q] == saero[q:N + q][::-1]:
                    if N > max:
                        max = N
            N -= 1
    return max

for tc in range(10):
    T = input()
    data = [input() for _ in range(100)]
    print(f'#{tc+1} {palind2(data)}')