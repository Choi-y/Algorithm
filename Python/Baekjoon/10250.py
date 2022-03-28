# ACM 호텔 (https://www.acmicpc.net/problem/10250)

# 입력 H: 층 수, W: 방의 수, N: 몇 번째 손님?
T = int(input())

answer = list()
for i in range(T):
    H, W, N = map(int, input().split())

    if N%H == 0:
        floor = H
        room = N//H
    else:
        floor = N%H
        room = N//H + 1

    if room < 10:
        answer.append(str(floor)+"0"+str(room))
    else:
        answer.append(str(floor)+str(room))

for i in answer:
    print(i)