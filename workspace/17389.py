# https://www.acmicpc.net/problem/17389 풀이

N = int(input())
S = input()

score = 0
correct = 0

for i in range(N):
    if S[i] == 'O':
        score += i + 1 + correct
        correct += 1
    elif S[i] == 'X':
        correct = 0

print(score)