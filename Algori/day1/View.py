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

    # for i in range(2, N-2):
    #     min = 987654321
    #     for j in range(5):
    #         if j != 2:
    #             if data[i] - data[i-2+j] < min:
    #                 min = data[i] - data[i-2+j]
    #     if min > 0:
    #         ans += min

    ############
    print("#{} {}".format(tc+1, ans))


