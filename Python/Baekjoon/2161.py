# https://www.acmicpc.net/problem/2161

num = int(input())
card_list = [str(x) for x in range(1, num+1)]

answer = []

while 1:
    answer.append(card_list.pop(0))
    if len(card_list) == 0:
        break
    card_list.append(card_list.pop(0))

print(' '.join(answer))
