# 오답

import sys
sys.stdin = open('sample_input.txt')


def dfs(idx):
    global cnt
    visited[idx] = True
    cnt += 1
    for i in graph[idx]:
        if not visited[i]:
            dfs(i)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = 0
    for i in range(N+1):
        cnt = 0
        if not visited[i]:
            dfs(i)
            if cnt > ans:
                ans = cnt

    print('#{} {}'.format(tc, ans))
