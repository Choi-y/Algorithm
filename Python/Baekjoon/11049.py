# 숫자 야구 (https://www.acmicpc.net/problem/2503) 풀이
# 희망과 빛의 도움을 받고 풀엇습니당......
n = int(input())
qsb = list()
for i in range(n):
    qsb.append(list(map(int, input().split())))

result = 0
for i in range(100, 1000):
    flag = True
    cand = str(i)
    if '0' in cand or len(set(cand)) != 3:
        continue
    for j in qsb:
        st = 0
        b = 0
        target = str(j[0])
        for k in range(3):
            if target[k] == cand[k]:
                st+=1
            else:
                if target[k] in cand:
                    b+=1
        if st != j[1] or b != j[2]:
            flag = False
            break
    if flag:
        result += 1

print(result)