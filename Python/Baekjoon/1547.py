# https://www.acmicpc.net/problem/1547 풀이

n = int(input())

cup_list = [0, 1,2,3]
for _ in range(n):
    a, b = map(int, input().split())
    
    a_index = cup_list.index(a)
    b_index = cup_list.index(b)
    
    tmp = cup_list[a_index]
    cup_list[a_index] = cup_list[b_index]
    cup_list[b_index] = tmp
    

print(cup_list[1])
