def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False
def calAbs(y, x):
    if y - x > 0: return y - x
    else: return x - y

arr = [[0 for _ in range(5)] for _ in range(5)]
for i in range(5):
    arr[i] = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

print(arr)

sum = 0
for y in range(len(arr)):
    for x in range(len(arr[0])):                    # 길이가 같으니까 0해도 무관
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if isWall(testX, testY) == False:
                sum += calAbs(arr[y][x], arr[testY][testX])

print(f"sum = {sum}")