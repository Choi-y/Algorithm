# 수 찾기 (https://www.acmicpc.net/problem/1920) 풀이 (7/1)


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