# https://www.acmicpc.net/problem/15686 풀이
# 21/07/05 풀이, 오답 --> 조합 사용 X

import sys

N, M = map(int, input().split())

CITY = list()
CX = list()
CY = list()
HX = list()
HY = list()

for i in range(N):
    CITY.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if CITY[i][j] == 2:
            CX.append(i)
            CY.append(j)
        elif CITY[i][j] == 1:
            HX.append(i)
            HY.append(j)

TMP = list()
MIN = list()
CTMP = list()

for i in range(len(CX)):
    A = 0
    for j in range(len(HX)):
        A += abs(HX[j]-CX[i])+abs(HY[j]-CY[i])
    TMP.append(A)
    CTMP.append(i)

for i in range(M):
    a = TMP.index(min(TMP))
    for j in range(len(MIN)):
        if a >= MIN[j]:
            a += 1
    MIN.append(CTMP[a])
    TMP.remove(min(TMP))

SOL = list()
TMP.clear()

for i in range(len(HX)):
    A = sys.maxsize
    for j in MIN:
        A = min(A, abs(HX[i]-CX[j])+abs(HY[i]-CY[j]))
    SOL.append(A)

ANS = 0
for i in SOL:
    ANS += i

print(ANS)