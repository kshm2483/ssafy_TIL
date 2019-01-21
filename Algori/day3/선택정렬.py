def selectionSort(a):
    for i in range(0, len(a)-1):        # 최소값
        min = i                         # 초기값을 줌
        for j in range(i+1, len(a)):    # 초기값이 있음으로 1부터 값을 비교
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]

data = [64, 25, 10, 22, 11]
selectionSort(data)
print(data)