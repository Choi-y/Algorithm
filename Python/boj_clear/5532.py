# 백준 브론즈 뿌수기
# 방학 숙제: https://www.acmicpc.net/source/52084114

L = int(input()) # 방학
A = int(input()) # 수학 
B = int(input()) # 국어
C = int(input()) # 1일 수학
D = int(input()) # 1일 국어

print(int(L-max(A/C, B/D)))
