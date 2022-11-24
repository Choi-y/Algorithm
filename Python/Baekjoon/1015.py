# https://www.acmicpc.net/problem/1015 수열 정렬

import copy

n = int(input())

a = list(input().split())
a_list = [int(x) for x in a]

b_list = copy.deepcopy(a_list)

b_list.sort()

answer = []
for i in range(n):
    answer.append(str(b_list.index(a_list[i])))
    b_list[b_list.index(a_list[i])] = -1
    
print(' '.join(answer))
