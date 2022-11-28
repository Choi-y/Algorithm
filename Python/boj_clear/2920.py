# https://www.acmicpc.net/problem/2920

import copy

origin = list(input().split())

asc_list = copy.deepcopy(origin)
desc_list = copy.deepcopy(origin)

asc_list.sort()
desc_list.sort(reverse=True)

if origin == asc_list:
  print("ascending")
elif origin == desc_list:
  print("descending")
else:
  print("mixed")