N = int(input())
vote = [list(map(int, input().split())) for _ in range(N)]

jaeyong = [[], [], []]
score = [[], [], []]

for i in range(3):
    votee = []
    for j in range(N):
        votee.append(vote[j][i])
    jaeyong[i] = votee

    one, two, thr = 0, 0, 0
    for k in range(N):
        if jaeyong[i][k] == 1:
            one += 1
        elif jaeyong[i][k] == 2:
            two += 1
        else:
            thr += 1

    jaeyong[i] = [one, two, thr]

for i in range(3):
    jaeyong[i].append((jaeyong[i][0]) + (jaeyong[i][1] * 2) + (jaeyong[i][2] * 3))

maxs = 0
max3 = 0
max2 = 0
hae = 0

for i in range(3):
    if jaeyong[i][3] > maxs:
        maxs = jaeyong[i][3]
        max3 = jaeyong[i][2]
        max2 = jaeyong[i][1]
        hae = i + 1
    elif jaeyong[i][3] == maxs:
        if jaeyong[i][2] > max3:
            max3 = jaeyong[i][2]
            max2 = jaeyong[i][1]
            hae = i + 1
        elif jaeyong[i][2] == max3:
            if jaeyong[i][1] > max2:
                max3 = jaeyong[i][2]
                max2 = jaeyong[i][1]
                hae = i + 1
            else:
                hae = 0
print(hae, maxs)