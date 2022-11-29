# https://www.acmicpc.net/problem/5596

S = list(input().split())
T = list(input().split())

S_total = 0; T_total = 0
for i in range(4):
    S_total += int(S[i])
    T_total += int(T[i])

print(max(S_total, T_total))