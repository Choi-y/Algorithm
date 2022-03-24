# 팩토리얼 (https://www.acmicpc.net/problem/10872) 풀이 (7/30)

# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

N = int(input())

factorial =1
if N!=0:
	for i in range(1, N+1):
		factorial *= i

print(factorial)
