# https://www.acmicpc.net/problem/1026 풀이

n = int(input())


a = input().split()
b = input().split()
    
for i in range(n):
    a[i] = int(a[i]); b[i] = int(b[i])
        
a.sort(); b.sort(reverse=True)
    
answer = 0
for i in range(n):
    answer += a[i]*b[i]
    
print(answer)
