import math

# 과일 서리 (https://www.acmicpc.net/problem/17213) 풀이

# N개의 종류 과일을 총 M개 훔치자! 그런데 종류별로 하나씩은 꼭 훔쳐야 해
# 그럼 종류별로 하나씩 훔치고, 나머지 M-N개를 다시 N개로부터 중복조합으로 뽑을까?
# 중복 조합은 nHr = n+r-1Cr이다.
# n+r-1Cr = (n+r-1)! / r!(n+r-1-r)!
# 정리하면 (n+r-1)! / r!(n-1)!
# 다시 정리하면... (n+r-1)부터 n까지 곱한 것! 나누기 r!이다
# math 라이브러리의 comb 함수 몰라, 그냥 무식하게 곱하자 --> 1번 방법
# 이럴 때 쓰라고 있는 라이브러리다! 사용하자 --> 2번 방법

N = int(input())
M = int(input())

# 1번 -> 조합을 그냥 곱하자!!
total = 1
for i in range(M-N+1, M):
    total *= i

for i in range(1, N):
    total /= i
print(int(total))

# 2번 -> 조합 라이브러리 쓰자!!
print(math.comb(M-1, M-N))