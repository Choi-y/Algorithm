# https://www.acmicpc.net/problem/2609 풀이

A, B = map(int, input().split())

for i in range(1, min(A, B)+1):
	if (A%i == 0) and (B%i == 0):
		MAX = i

j = max(A, B)
while(1):
	if (j%A == 0) and (j%B == 0):
		MIN = j
		break
	j += 1

print(MAX)
print(MIN)
