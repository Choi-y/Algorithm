# 수 정렬하기 2 (https://www.acmicpc.net/problem/2751)
import sys

N = int(input())

num_list = list()
for _ in range(N):
    num_list.append(int(sys.stdin.readline())) ## 입력에 많은 시간 쓰지 않게!

num_list.sort()

for num in num_list:
    print(num)