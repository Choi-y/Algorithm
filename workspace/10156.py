# https://www.acmicpc.net/problem/10156 풀이

K, N, M = map(int, input().split())

if M < K*N:
	print(K*N-M)
else:
	print(0)
