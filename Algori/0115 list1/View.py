import sys
sys.stdin = open("View_input.txt")
T = 10
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))

    ############

    for i in range(len(data)):
        if data[i] > data[i-1] and data[i] > data[i-2]:
            if data[i] > data[i+1] and data[i] > data[i+2]:
                ans += (data[i] - max(data[i-1], data[i-2], data[i+1], data[i+2]))
                # ans = data[i] - max(data[i-1], data[i-2], data[i+1], data[i+2])

    ############
    print("#{} {}".format(tc+1, ans))