# https://www.acmicpc.net/problem/22114 풀이

# N = 빨간색 보도블럭, K = 창영이 보폭
N, K = map(int, input().split())
L = list(map(int, input().split()))

SOL = list()

# 앞에서부터
for i in range(N-1):
    jump = 0
    red = 1
    for j in range(i, N-1):
        if L[j] <= K:
            red += 1
        elif L[j] > K:
            if jump == 0:
                red += 1
                jump += 1
            elif jump > 0:
                SOL.append(red)
                break
        SOL.append(red)

# # 뒤에서부터
for i in range(N-1, 0):
    jump = 0
    red = 1
    for j in range(i, 0):
        if L[j] <= K:
            red += 1
        elif L[j] > K:
            if jump == 0:
                red += 1
                jump += 1
            elif jump > 0:
                SOL.append(red)
                break
        SOL.append(red)

print(max(SOL))