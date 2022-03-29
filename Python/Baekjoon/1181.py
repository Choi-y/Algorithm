# 단어 정렬 (https://www.acmicpc.net/problem/1181)

N = int(input())

dict = {}
for _ in range(N):
    str = input()
    dict[str] = len(str)

sort_key = sorted(dict.items())
sort_key.sort(key=lambda x:x[1])

for i in sort_key:
    print(i[0])
