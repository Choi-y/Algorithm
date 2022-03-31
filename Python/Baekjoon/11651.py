# 좌표 정렬하기 (https://www.acmicpc.net/problem/11650)

T = int(input())
dot = list()
for _ in range(T):
    dot.append(list(map(int, input().split())))

dot.sort(key=lambda x:(x[1], x[0]))
for d in dot:
    print(*d)