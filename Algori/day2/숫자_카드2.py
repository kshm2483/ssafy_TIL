import sys
sys.stdin = open("sample2_input.txt")

T = int(input())
for tc in range(T):
   ans = 0 # 카드의 중첩 수
   ans2 = 0 # 카드에 적힌 수
   N = int(input())
   data = []
   data.extend(input()) # 뽑힌 카드의 번호
   count = [0]*10 # 카드의 중첩 수
   K = [0]*10 # 카드에 적힌 수

   for i in range(len(data)): # 데이터의 길이만큼
       K[int(data[i])] = int(data[i])
       count[int(data[i])] += 1
       for j in range(len(count)):
           if ans < count[j]:
               ans = count[j]
           for z in range(len(K)):
               if ans < count[z]:
                   ans2 = K[z]
               if ans == count[z]:
                   if ans2 < K[z]:
                       ans2 = K[z]
   print(f'#{tc+1} {ans2} {ans}')