# 개선 필요
# https://www.acmicpc.net/problem/16205 풀이

## 1 - Camel, 2 - Snake, 3 - Pascal
N, S = input().split()

point = [0]
if (N == "1"):
	result=list()
	for i in range(len(S)):
		if (S[i].isupper() == 1):
			point.append(i)
	for i in range(len(point)):
		if i == len(point)-1:
			result.append(S[point[i]:])
		else:
			result.append(S[point[i]:point[i+1]])

elif (N == "2"):
	result = S.split('_')

elif (N == "3"):
	result = list()
	for i in range(1,len(S)):
		if (S[i].isupper() == 1):
			point.append(i)
	for i in range(len(point)):
		if i == len(point)-1:
			result.append(S[point[i]:])
		else:
			result.append(S[point[i]:point[i+1]])
			
### 출력
# 1번 카멜
camel = [i.capitalize() for i in result]
camel[0] = camel[0].lower()

# 2번 스네이크
snake = [i.lower() for i in result]

# 3번 파스칼
pascal = [i.capitalize() for i in result]

print("".join(camel) + "\n" + "_".join(snake) + "\n" + "".join(pascal))
