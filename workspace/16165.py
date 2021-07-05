# https://www.acmicpc.net/problem/16165 풀이

# N = 걸그룹 수, M 맞혀야 할 문제 수
N, M = map(int, input().split())

TEAMNAME = list()
TEAM = list()

# 입력
for i in range(N):
    a = input()
    TEAMNAME.append(a)
    TEAM.append(a)
    TEAM[i] = list()
    MEMBER = int(input())
    for j in range(MEMBER):
        TEAM[i].append(input())
        TEAM[i].sort()

SOL = list()

# 퀴즈
for i in range(M):
    Q = input()
    TYPE = int(input())

    # 팀 이름 출력
    if TYPE == 1:
        for j in range(N):
            if TEAM[j].count(Q) > 0:
                SOL.append(TEAMNAME[j])
                break
    # 멤버 이름 출력
    elif TYPE == 0:
        S = TEAMNAME.index(Q)
        for j in range(len(TEAM[S])):
            SOL.append(TEAM[S][j])

for i in range(len(SOL)):
    print(SOL[i])