# 나는 요리사다 (https://www.acmicpc.net/problem/2953) 풀이 (8/2)

# "나는 요리사다"는 다섯 참가자들이 서로의 요리 실력을 뽐내는 티비 프로이다. 각 참가자는 자신있는 음식을 하나씩 만들어오고, 서로 다른 사람의 음식을 점수로 평가해준다. 점수는 1점부터 5점까지 있다.
# 각 참가자가 얻은 점수는 다른 사람이 평가해 준 점수의 합이다. 이 쇼의 우승자는 가장 많은 점수를 얻은 사람이 된다.
# 각 참가자가 얻은 평가 점수가 주어졌을 때, 우승자와 그의 점수를 구하는 프로그램을 작성하시오.

# 입력: 다섯 줄에 각 참가자가 얻은 네 개의 평가 점수가 공백으로 구분돼 주어짐
# 출력: 첫째 줄에 우승자의 번호와 받은 점수 출력

score = list()

for i in range(5):
	A, B, C, D = map(int, input().split())
	tmp = A+B+C+D
	score.append(tmp)

max_score = max(score)
win = score.index(max_score) + 1

print('%d %d' % (win, max_score))
