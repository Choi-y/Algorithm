# https://www.acmicpc.net/problem/21866 풀이

max_list = [100,100,200,200,300,300,400,400,500]
score_list = list(map(int, input().split()))
is_hacker = False

if sum(score_list) < 100:
    print("none")

else:
    for i in range(9):
        if score_list[i] > max_list[i]:
            is_hacker = True
            break
            
    if is_hacker == True:
        print("hacker")
    else:
        print("draw")
