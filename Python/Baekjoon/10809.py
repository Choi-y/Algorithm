# 알파벳 찾기 (https://www.acmicpc.net/problem/10809) 풀이 (7/5)

# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = list(input()) # 문자 입력받아서 리스트에 삽입
sol = list() # 정답 넣을 리스트 생성
for i in range(26): # 알파벳 수만큼 for문 실행
    if S.count(chr(97+i)) > 0: # chr(97) = 'a'이므로, +i 해 주면 a부터 z까지 순서대로 확인 가능
        sol.append(S.index(chr(97+i))) # 리스트 S 안에 해당하는 알파벳이 있다면 위치를 정답 리스트에 삽입
    else:
        sol.append(-1) # 리스트 안에 해당 알파벳이 없다면 -1 삽입

for i in range(26):
    print(str(sol[i]), end=" ") # 순서대로 출력, 띄어쓰기로 구분