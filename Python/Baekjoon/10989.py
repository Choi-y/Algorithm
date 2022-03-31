# 수 정렬하기 3 (https://www.acmicpc.net/problem/10989)
import sys

N = int(input())

## 그냥 평소처럼 무식하게 풀면 메모리 초과 뜬다,,,
num_list = [0]*10001
for _ in range(N):
    a = int(sys.stdin.readline())
    num_list[a] += 1

for i in range(1,10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)