# https://www.acmicpc.net/problem/2581 풀이

M = int(input())
N = int(input())

sol = 0
DEC = list()
for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                count += 1
                break
        if count == 0:
            DEC.append(i)

if len(DEC) == 0:
    print("-1")
else:
    print(sum(DEC))
    print(min(DEC))