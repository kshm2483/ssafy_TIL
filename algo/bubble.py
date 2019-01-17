def bubblesort(x):
    length = len(x) - 1
    for i in range(length):
        for j in range(length - i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]

bubblesort([3,7,4,5,1,9,8])