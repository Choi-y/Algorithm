# programmers 해시 1: 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

#answer=list(set(participant)-set(completion))

#for i in completion:
#    if i in participant:
#        participant.remove(i)
#answer = ''.join(participant)

dict = {}
for i in participant:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

for i in completion:
    dict[i] -= 1

for key, val in dict.items():
    if val == 1:
        answer = key

print(answer)