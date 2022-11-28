# https://www.acmicpc.net/problem/1157

alpha = list(input().upper())

alpha_element = set(alpha)

ans = list()
max_count = 0
for ae in alpha_element:
  ans.append([ae, alpha.count(ae)])
  max_count = max(max_count, alpha.count(ae))

answer = list()
for i in range(len(ans)):
  if ans[i][1] == max_count:
    answer.append(ans[i])

if len(answer) == 1:
  print(answer[0][0])
else:
  print("?")