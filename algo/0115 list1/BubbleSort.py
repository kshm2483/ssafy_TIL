def bubblesort(data):
    for i in range(len(data)-1, 0, -1): # 4 3 2 1
        for j in range(0, i): # 4 3 2 1
            if data[j] < data[j+1]: # 정렬 방향
                data[j], data[j+1] = data[j+1], data[j]
data = [55, 7, 78, 12, 42]
bubblesort(data)
print(data)