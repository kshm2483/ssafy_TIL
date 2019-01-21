def binarySearch(a, key):
    start = 0
    end = len(a)
    while start <= end :
        middle = (start + end)//2   # 절반찾기
        if a[middle] == key:
            return middle           # key의 위치 리턴
        elif  a[middle] > key:      # 키보다 큰값 버리기
            end = middle - 1
        else: start = middle + 1    # 키보다 작은값 버리기
    return -1

key = 7
data = [2, 4, 7, 9, 11, 19, 23]
print(binarySearch(data, key))