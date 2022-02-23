# 피보나치수 (https://www.acmicpc.net/problem/10870)

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램
# 입력: 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0
# 출력: 첫째 줄에 n번째 피보나치 수를 출력

n = int(input())

fibo = [0, 1]
for i in range(2, n+1):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[n])