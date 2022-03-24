# 수 찾기 (https://www.acmicpc.net/problem/1920) 풀이 (7/1)

# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start+end)//2
        if x == a[mid]:
            return 1
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

for i in range(M):
    print(binary_search(A, B[i]))