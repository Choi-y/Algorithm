# https://www.acmicpc.net/problem/9037 풀이

# 테스트 케이스 T
T = int(input())
SOL = list()

for i in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    solution = -1

    while(1):
        # 짝수 맞춰 주는 과정
        for j in range(N):
            if C[j] % 2 == 1:
                C[j] += 1

        solution += 1
        if C.count(C[0]) == N:
            break

        # 옆으로 주는 과정
        tmp = list()
        for j in range(N):
            tmp.append(C[j]//2)
            C[j] -= tmp[j]

        C[0] = C[0] + tmp[N-1]
        for j in range(N-1):
            C[j+1] += tmp[j]

    SOL.append(solution)

for i in range(T):
    print(SOL[i])