# 소인수분해 (https://www.acmicpc.net/problem/11653) 풀이 (7/31)

# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

N = int(input())

i = 2
while(1):
   if (N % i == 0):
      print(i)
      N = N // i
   else:
      i += 1

   if (N == 1) or (i > N):
      break
