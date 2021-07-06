import sys

N, M = map(int, sys.stdin.readline().split())

awful = []

for i in range(N+1):
    awful.append([0]*(N+1))

for i in range(M):
    combination = list(map(int, sys.stdin.readline().split()))
    if combination[0] > combination[1]:
        combination[0], combination[1] = combination[1], combination[0]
    awful[combination[0]][combination[1]] = 1

cnt = 0
select = []

for i in range(1, N-1):
    select.append(i)    
    for j in range(i+1, N):
        if awful[select[0]][j] != 1:
            select.append(j)
            for k in range(j+1, N+1):
                if awful[select[0]][k] != 1 and awful[select[1]][k] != 1:
                    select.append(k)
                    if len(select) == 3:
                        cnt += 1
                        select.pop()
            if len(select) == 2:
                select.pop()
    if len(select) == 1:
            select.pop()

print(cnt)
                    
