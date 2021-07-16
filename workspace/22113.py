# https://www.acmicpc.net/problem/22113 풀이

# N = 버스 개수, M = 창영이가 이용하는 버스 개수
N, M = map(int, input().split())

# 창영이가 이용하는 버스를 리스트에 넣는다
bus_list = list(map(int, input().split()))

# fee는 환승 요금에 대한 정보, 2차원 배열
fee = list()
for i in range(N):
    fee.append(list(map(int, input().split())))

# 요금을 다 더해 줄 변수 SUM
SUM = 0
for i in range(len(bus_list)-1):
    SUM += fee[bus_list[i]-1][bus_list[i+1]-1]

print(SUM)