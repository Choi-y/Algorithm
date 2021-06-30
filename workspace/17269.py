# https://www.acmicpc.net/problem/17269 풀이

num1, num2 = input().split()

num1 = int(num1)
num2 = int(num2)

a = list()
b = list()

name1, name2 = input().split()

for i in range(num1):
    if name1[i] in ["A", "F", "H", "K", "M"]:
        a.append(3)
    elif name1[i] in ["B", "D", "N", "P", "Q", "R", "T", "X", "Y"]:
        a.append(2)
    elif name1[i] in ["C", "G", "I", "J", "L", "O", "S", "U", "V", "W", "Z"]:
        a.append(1)
    elif name1[i] in ["E"]:
        a.append(4)

for j in range(num2):
    if name2[j] in ["A", "F", "H", "K", "M"]:
        b.append(3)
    elif name2[j] in ["B", "D", "N", "P", "Q", "R", "T", "X", "Y"]:
        b.append(2)
    elif name2[j] in ["C", "G", "I", "J", "L", "O", "S", "U", "V", "W", "Z"]:
        b.append(1)
    elif name2[j] in ["E"]:
        b.append(4)

sum = num1 + num2
trey = list()

if num1 > num2:
    for i in range(num2):
        trey.append(a[i])
        trey.append(b[i])
    for j in range(num1-num2):
        trey.append(a[num2+j])
elif num2 > num1:
    for i in range(num1):
        trey.append(a[i])
        trey.append(b[i])
    for j in range(num2-num1):
        trey.append(b[num1 + j])
elif num1 == num2:
    for i in range(num1):
        trey.append(a[i])
        trey.append(b[i])

sol = list()

for i in range(sum-2):
    for j in range(sum-1-i):
        yj = trey[j]+trey[j+1]
        if yj >= 10:
            yj %= 10
        sol.append(yj)

    if (i == sum-3):
        break

    trey.clear()
    for k in range(len(sol)):
        trey.append(sol[k])
    sol.clear()

if sol[0] == 0:
    print(str(sol[1])+"%")
else:
    print(str(sol[0])+str(sol[1])+"%")