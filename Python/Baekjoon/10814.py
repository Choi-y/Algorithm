# 나이순 정렬 (https://www.acmicpc.net/problem/10814)

N = int(input())
user = list()

for _ in range(N):
    user.append(input().split())

user.sort(key=lambda x:int(x[0]))
for i in user:
    print(*i)