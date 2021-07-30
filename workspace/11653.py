# https://www.acmicpc.net/problem/11653 풀이

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
