# https://www.acmicpc.net/problem/2475

num_list = list(map(int, input().split()))

ans = 0
for n in num_list:
  ans += pow(n, 2)
  
print(ans%10)