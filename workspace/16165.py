# 걸그룹 마스터 준석이 (https://www.acmicpc.net/problem/16165) 풀이 (7/4)

# 정우는 소문난 걸그룹 덕후이다. 정우의 친구 준석이도 걸그룹을 좋아하지만 이름을 잘 외우지 못한다는 문제가 있었다.
# 정우는 친구를 위해 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 퀴즈 프로그램을 만들고자 한다.

# N = 걸그룹 수, M 맞혀야 할 문제 수
N, M = map(int, input().split())

team_name = list()
team = list()

# 입력
for i in range(N):
    a = input()
    team_name.append(a)
    team.append(a)
    team[i] = list()
    member = int(input())
    for j in range(member):
        team[i].append(input())
        team[i].sort()

sol = list()

# 퀴즈
for i in range(M):
    Q = input()
    type = int(input())

    # 팀 이름 출력
    if type == 1:
        for j in range(N):
            if team[j].count(Q) > 0:
                sol.append(team_name[j])
                break
    # 멤버 이름 출력
    elif type == 0:
        S = team_name.index(Q)
        for j in range(len(team[S])):
            sol.append(team[S][j])

for i in range(len(sol)):
    print(sol[i])