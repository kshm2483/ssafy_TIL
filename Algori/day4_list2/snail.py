data = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]
        ]
arr = []
snail = []
dx = []
dy = []
for y in range(len(data)):
    for x in range(len(data[y])):
        arr.append(data[x][y])
arr.sort(reverse=True)

def isWall(x, y):
    if x < 0 or x >= 5 : return True
    if y < 0 or y >= 5 : return True
    return False

for y in range(len(data)):
    for x in range(len(data[y])):
