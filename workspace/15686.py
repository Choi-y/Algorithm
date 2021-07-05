# https://www.acmicpc.net/problem/15686 풀이
# 21/07/05 조합 함수(combinations) 사용
import sys
from itertools import combinations

N, M = map(int, input().split())

CITY = list()
CHICKEN = list()
HOME = list()

for i in range(N):
    CITY.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if CITY[i][j] == 2:
            CHICKEN.append([i, j])
        elif CITY[i][j] == 1:
            HOME.append([i, j])

TMP = list(combinations(CHICKEN, M))

SOL = [0 for i in range(len(TMP))]

for i in HOME:
    TEMP = 0
    for j in range(len(TMP)):
        A = sys.maxsize
        for k in TMP[j]:
            A = min(A, abs(i[0] - k[0]) + abs(i[1] - k[1]))
        SOL[j] += A

print(min(SOL))