# 숫자의 합 (https://www.acmicpc.net/problem/11720) 풀이 (7/30)

# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N=int(input())
S=list(input())

number=list()
for i in range(N):
	number.append(int(S[i]))

print(sum(number))