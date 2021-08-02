# https://www.acmicpc.net/problem/2953 풀이

score = list()

for i in range(5):
	A, B, C, D = map(int, input().split())
	tmp = A+B+C+D
	score.append(tmp)

max_score = max(score)
win = score.index(max_score) + 1

print('%d %d' % (win, max_score))
