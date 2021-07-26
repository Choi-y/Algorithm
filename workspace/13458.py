# https://www.acmicpc.net/problem/13458 풀이

# N = 시험장
N = int(input())
# 시험장 응시자 수
A = list(map(int, input().split()))
# B = 총감독, C = 부감독
B, C = map(int, input().split())

SOL = 0

for i in range(N):
    A[i] = A[i] - B
    SOL += 1

    if (A[i] > 0):
        SOL += A[i]//C
        if (A[i] % C > 0):
            SOL += 1

print(SOL)