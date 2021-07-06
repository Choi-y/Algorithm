# https://www.acmicpc.net/problem/2839 풀이

N = int(input())

SOL = list()
i = 0

#while (N - 5*i >= 0):
for i in range(N//5+1):
    if (N - 5*i) % 3 == 0:
        SOL.append(i + (N-5*i)//3)
#    i += 1

if len(SOL) != 0:
    print(min(SOL))
else:
    print("-1")