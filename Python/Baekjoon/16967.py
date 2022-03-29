# 배열 복원하기 (https://www.acmicpc.net/problem/16967)

H, W, X, Y = map(int, input().split())

B = list()
for _ in range(H+X):
    B.append(list(map(int, input().split())))

A = list()
## 아무것도 안 더해진 A
for i in range(X):
    A.append(B[i][:W])

## 더해진 A
for i in range(H-X):
    for j in range(W-Y):
        B[i+X][j+Y] -= A[i][j]
    A.append(B[i+X][:W])

for i in A:
    for j in i:
        print(j, end=" ")
    print()