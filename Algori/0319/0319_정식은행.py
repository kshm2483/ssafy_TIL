import sys
sys.stdin = open('0319_정식은행.txt')

for tc in range(int(input())):
    binnum = list(map(int, input()))
    trinum = list(map(int, input()))

    binans = []
    trians = []

    for i in range(len(binnum)):
        if binnum[i] == 1:
            binnum[i] = 0
            binans.append(int(''.join(map(str, binnum)), 2))
            binnum[i] = 1
        else:
            binnum[i] = 1
            binans.append(int(''.join(map(str, binnum)), 2))
            binnum[i] = 0

    for i in range(len(trinum)):
        if trinum[i] == 1:
            trinum[i] = 0
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 2
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 1
        elif trinum[i] == 2:
            trinum[i] = 0
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 1
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 2
        else:
            trinum[i] = 1
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 2
            trians.append(int(''.join(map(str, trinum)), 3))
            trinum[i] = 0

    ans = set(binans) & set(trians)
    print('#{} {}'.format(tc+1, *ans))