# https://www.acmicpc.net/problem/1712 풀이

A, B, C = map(int, input().split())

if C <= B:
	SOL = -1
else:
	SOL = A // (C-B) + 1

print(SOL)
