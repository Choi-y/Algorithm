# 최대공약수와 최소공배수 (https://www.acmicpc.net/problem/2609) 풀이

# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

A, B = map(int, input().split())

for i in range(1, min(A, B)+1):
	if (A%i == 0) and (B%i == 0):
		least_common_multiple = i

j = max(A, B)
while(1):
	if (j%A == 0) and (j%B == 0):
		greatest_common_factor = j
		break
	j += 1

print("%d\n%d" % (least_common_multiple, greatest_common_factor))