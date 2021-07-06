import sys


def dfs(ice_cream, select, number, cnt, awful):
    select.append(number)
    if len(select) == 3:
        cnt[0] += 1
    else:    
        for i in range(len(ice_cream[number])):
            if len(select) == 1 and not awful[select[0]][ice_cream[number][i]]:
                dfs(ice_cream, select, ice_cream[number][i], cnt, awful)
                select.pop()
            if len(select) == 2 and not awful[select[0]][ice_cream[number][i]] and not awful[ice_cream[number][i]][number]:
                    dfs(ice_cream, select, ice_cream[number][i], cnt, awful)
                    select.pop()



N, M = map(int, sys.stdin.readline().split())

awful = []
ice_cream = []

for i in range(N+1):
    ice_cream.append([])        
    awful.append([0]*(N+1))

for i in range(M):
    combination = list(map(int, sys.stdin.readline().split()))
    if combination[0] > combination[1]:
        combination[0], combination[1] = combination[1], combination[0]
    awful[combination[0]][combination[1]] = 1

for i in range(1, N):
    for j in range(i+1, N+1):
        if not awful[i][j]:
            ice_cream[i].append(j)
    
cnt = [0]

for i in range(1, N):
    dfs(ice_cream, [], i, cnt, awful)

print(cnt[0])


    
