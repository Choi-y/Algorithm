# https://www.acmicpc.net/problem/21867 풀이

N = int(input())
S = input()

count_a = S.count('A')
count_j = S.count('J')
count_v = S.count('V')

if count_a + count_j + count_v == 0:
    print(S)
    
else:
    S = S.replace("A", "")
    S = S.replace("J", "")
    S = S.replace("V", "")
    
    if len(S) > 0:
        print(S)
    elif len(S) == 0:
        print("nojava")
