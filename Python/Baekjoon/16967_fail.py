# 배열 복원하기 (https://www.acmicpc.net/problem/16967)
# 반례 https://www.acmicpc.net/board/view/87303 여기서 걸려서 틀림

H, W, X, Y = map(int, input().split())

B = list()
for _ in range(H+X):
    B.append(list(input().split()))

A = list()
for i in range(X):
    A.append(B[i][:W-Y+1])

for i in range(H, H+X):
    A.append(B[i][Y:])

answer = list()
for a in A:
    if a not in answer:
        answer.append(a)

for i in answer:
    print(" ".join(i))