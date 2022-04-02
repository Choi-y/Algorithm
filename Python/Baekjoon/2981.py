# 검문 (https://www.acmicpc.net/problem/2981)
# 빛~~~
import math

N = int(input())

nl = [int(input()) for x in range(N)]
nl.sort()

rl = list()
for i in range(1, N):
    rl.append(nl[i] - nl[i-1])
rl.sort()

val = rl[0]
for i in range(1, len(rl)):
    val = math.gcd(val, rl[i])

answer = list()
for i in range(2, int(math.sqrt(val))+1):
    if i * i == val:
        answer.append(i)
    elif val % i == 0:
        answer.append(i)
        answer.append(val//i)

answer.append(val)
answer.sort()
print(*answer)