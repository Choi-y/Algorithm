# 개선 필요
# 변수명 (https://www.acmicpc.net/problem/16205) 풀이 (8/2)

# 변수명을 정하는 표기법은 여러 가지가 있다.
#
# 카멜 표기법 (Camel Case): 각 단어의 첫 글자를 대문자로 적는다. 단, 가장 첫 글자는 소문자를 사용한다.
#  - 예시: camelCase, variableN, thisIsCamelCase, howToSolveThisProblem
# 스네이크 표기법 (Snake Case): 소문자만 사용하고, 각 단어의 사이에 언더바(_)를 넣어서 적는다.
#  - 예시: snake_case, variable_n, this_is_snake_case, how_to_solve_this_problem
# 파스칼 표기법 (Pascal Case): 카멜 표기법과 같지만, 가장 첫 글자도 대문자를 사용한다.
#  - 예시: PascalCase, VariableN, ThisIsPascalCase, HowToSolveThisProblem
# 한 표기법을 사용한 변수명이 주어졌을 때, 이를 다른 표기법으로 변환하는 프로그램을 작성하시오.

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
