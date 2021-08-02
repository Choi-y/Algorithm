# https://www.acmicpc.net/problem/1085 풀이

X, Y, W, H = map(int, input().split())

SOL = list()
## 좌우로 탈출 X, W
if ((X-0) <= (W-X)):
	SOL.append(X-0)
else:
	SOL.append(W-X)

## 상하로 탈출 Y, H
if ((Y-0) <= (H-Y)):
	SOL.append(Y-0)
else:
	SOL.append(H-Y)

print(min(SOL))
