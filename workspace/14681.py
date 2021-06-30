# https://www.acmicpc.net/problem/14681 문제 풀이

x = int(input())
y = int(input())

# 첫 번째
if x*y > 0:
    if x>0:
        a = 1
    else:
        a = 3
else:
    if x>0:
        a = 4
    else:
        a = 2

# 두 번째
if x > 0 and y > 0:
    a = 1
elif x < 0 and y > 0:
    a = 2
elif x < 0 and y < 0:
    a = 3
elif x > 0 and y < 0:
    a = 4

print(a)