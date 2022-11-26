# https://www.acmicpc.net/problem/11536

import copy

n = int(input())

name_list = []
for i in range(n):
    name_list.append(input())
    
comp_list_in = copy.deepcopy(name_list)
comp_list_de = copy.deepcopy(name_list)

comp_list_in.sort(); comp_list_de.sort(reverse=True)

if comp_list_in == name_list:
    print("INCREASING")
    
elif comp_list_de == name_list:
    print("DECREASING")
    
else:
    print("NEITHER")
