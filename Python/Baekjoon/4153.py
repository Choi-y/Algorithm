# 직각삼각형 (https://www.acmicpc.net/problem/4153)

answer = list()
while True:
    x = input()
    if x == "0 0 0":
        break

    abc = list(map(int, x.split()))
    abc.sort()
    a = abc[0]; b = abc[1]; c = abc[2]

    if c*c == a*a + b*b:
        answer.append("right")
    else:
        answer.append("wrong")

for i in answer:
    print(i)