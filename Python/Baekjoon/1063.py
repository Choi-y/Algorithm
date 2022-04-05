# 킹(https://www.acmicpc.net/problem/1063)
K, S, N = input().split()
K = list(K); S = list(S); N = int(N)

## 위치
def position(a, b):
    return ord(a)-65, int(b)-1

K[0], K[1] = position(K[0], K[1])
S[0], S[1] = position(S[0], S[1])

def move_to(L, move):
    x = L[0]; y = L[1]
    if move == 'R': #오른쪽으로 한칸
        x += 1
    elif move == 'L': # 왼쪽 한칸
        x -= 1
    elif move == 'B': # 한칸 아래
        y -= 1
    elif move == 'T': # 한칸 위
        y += 1
    elif move == 'RT': #오른쪽 위 대각선
        x += 1
        y += 1
    elif move == 'LT': # 왼쪽 위 대각선
        x -= 1
        y += 1
    elif move == 'RB': #오른쪽 아래 대각선
        x += 1
        y -= 1
    elif move == 'LB': # 왼쪽 아래 대각선
        x -= 1
        y -= 1

    return x, y

def discriminate(li, mov):
    x, y = move_to(li, mov)
    if li == K:
        if x == S[0] and y == S[1]:
            xs, ys = move_to(S, mov)
            if xs >= 0 and ys >= 0 and xs < 8 and ys < 8:
                S[0] = xs
                S[1] = ys
                K[0] = x
                K[1] = y
        else:
            if x >= 0 and y >= 0 and x < 8 and y < 8:
                K[0] = x
                K[1] = y

for _ in range(N):
    move = input()
    ### 함수 넣자
    discriminate(K, move)

#############################
def position_to_alpha(a, b):
    x = a+65
    return chr(x)+str(int(b)+1)
###########################################

print(position_to_alpha(K[0], K[1]))
print(position_to_alpha(S[0], S[1]))