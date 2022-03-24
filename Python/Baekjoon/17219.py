# 비밀번호 찾기 (https://www.acmicpc.net/problem/17219) 풀이 (8/2)

N, M = map(int, input().split())

pwd = dict()
for i in range(N):
    a, b = input().split()

    pwd[a] = b

so_list = list()
for i in range(M):
    so_list.append(input())

for i in range(M):
    print(pwd[so_list[i]])