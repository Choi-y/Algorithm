# https://www.acmicpc.net/problem/1476 풀이

# E - 지구 / S - 태양 / M - 달
E, S, M = map(int, input().split())

if (E == 15):
    E = 0
if (S == 28):
    S = 0
if (M == 19):
    M = 0

i = 0
while(1):
    i += 1
    if ((E == i % 15) and (S == i % 28) and (M == i % 19)):
        SOL = i
        break

print(SOL)