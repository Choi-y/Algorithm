# 직사각형에서 탈출 (https://www.acmicpc.net/problem/1085)

# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

# 입력: X, Y, W, H
# 출력: 직사각형 경계선까지 가는 거리의 최솟값

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
