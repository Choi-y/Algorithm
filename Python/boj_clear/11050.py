# https://www.acmicpc.net/problem/11050

N, K = map(int, input().split())

child = 1
mom = 1
for i in range(N, N-K, -1):
    child *= i

for j in range(K, 0, -1):
    mom *= j
    
print(child//mom)