# Java Bitecode (https://www.acmicpc.net/problem/21867) 풀이 (7/22)

# 그래서 태한이는 코딩을 할 때 알파벳 J, A, V는 사용하지 않는다. 또한 기존의 코드에서도 J, A, V가 보이면 전부 이빨로 깨물어 제거한다.
# 기존의 코드에서 J, A, V를 깨물어 제거한 코드를 JAVA Bitecode라고 부른다.
# 입력으로 길이가 N인 코드 S가 주어지면, 그 코드의 JAVA Bitecode를 구해보자!

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
