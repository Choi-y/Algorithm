# https://www.acmicpc.net/problem/11720 풀이

N=int(input())
S=list(input())

NUMBER=list()
for i in range(N):
	NUMBER.append(int(S[i]))

print(sum(NUMBER))
