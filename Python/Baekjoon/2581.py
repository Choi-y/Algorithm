# 소수 (https://www.acmicpc.net/problem/2581) 풀이

# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

M = int(input())
N = int(input())

sol = 0
prime_number = list()
for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                count += 1
                break
        if count == 0:
            prime_number.append(i)

if len(prime_number) == 0:
    print("-1")
else:
    print("%d\n%d" % (sum(prime_number), min(prime_number)))