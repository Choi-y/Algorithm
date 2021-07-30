# https://www.acmicpc.net/problem/10872 풀이

N = int(input())

fac=1
if N==0:
	fac=1
else:
	for i in range(1, N+1):
		fac *= i

print(fac)
