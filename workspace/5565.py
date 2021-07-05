# https://www.acmicpc.net/problem/5565 풀이

SOL = int(input())
PRICE = list()

for i in range(9):
    PRICE.append(int(input()))
    SOL -= PRICE[i]

print(SOL)