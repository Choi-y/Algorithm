# https://www.acmicpc.net/problem/5635

n = int(input())

birth_list = []
for i in range(n):
    name, day, month, year = input().split()
    birth_list.append([name, int(day), int(month), int(year)])
    
birth_list.sort(key=lambda x:(x[3], x[2], x[1]))

print(birth_list[-1][0])
print(birth_list[0][0])
