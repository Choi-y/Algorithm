# https://www.acmicpc.net/problem/17224 풀이

# N=문제 수, L=역량, K=풀 수 있는 최대 문제 수
N, L, K = map(int, input().split())

SOL = 0

sub1 = list()
sub2 = list()

for i in range(N):
    a, b = map(int, input().split())
    if b > L:
        if a <= L:
            sub1.append(a)
    elif b <= L:
        sub2.append(b)

score = min(K, len(sub2)) * 140
if K > len(sub2):
    score += min((K-len(sub2)), len(sub1)) * 100

print(score)