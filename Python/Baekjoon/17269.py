## 개선 필요
# 이름궁합 테스트 (https://www.acmicpc.net/problem/17269) 풀이 (6/30)

# 이름궁합을 보는 방법은 간단하다. 먼저 이름을 알파벳 대문자로 적는다. 각 알파벳 대문자에는 다음과 같이 알파벳을 적는데 필요한 획수가 주어진다.
# 알파벳을 대응하는 숫자로 바꾸고 각 숫자와 그 숫자의 오른쪽 숫자와 더한 것을 밑에 적는다. 더한 숫자가 10이 넘을 경우엔 일의 자리 수만 남긴다. 이 과정을 반복하여 숫자가 2개만 남았을 때 남은 숫자가 두 사람의 궁합이 좋을 확률이 된다.

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