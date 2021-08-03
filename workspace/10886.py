# 0 = not cute / 1 = cute (https://www.acmicpc.net/problem/10886) 풀이 (8/2)

# 준희는 자기가 팀에서 귀여움을 담당하고 있다고 생각한다.
# 하지만 연수가 볼 때 그 의견은 뭔가 좀 잘못된 것 같았다. 그렇기에 설문조사를 하여 준희가 귀여운지 아닌지 알아보기로 했다.

N = int(input())

is_cute = 0
for i in range(N):
	is_cute += int(input())

if is_cute > N//2:
	print("Junhee is cute!")
else:
	print("Junhee is not cute!")
