# https://www.acmicpc.net/problem/18258

# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

N = int(input())

comm = list()
q = list()
for i in range(N):
    cl = input()

    if ' ' in cl:
        p, n = cl.split()
        q.append(n)
    elif cl == 'pop':
        if len(q) == 0:
            comm.append(-1)
        else:
            comm.append(q[0])
            del q[0]
    elif cl == 'size':
        comm.append(len(q))
    elif cl == 'empty':
        if len(q) == 0:
            comm.append(1)
        else:
            comm.append(0)
    elif cl == 'front':
        if len(q) == 0:
            comm.append(-1)
        else:
            comm.append(q[0])
    elif cl == 'back':
        if len(q) == 0:
            comm.append(-1)
        else:
            comm.append(q[len(q) - 1])

for i in comm:
    print(i)