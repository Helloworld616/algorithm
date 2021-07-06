# 정답

import sys
sys.stdin = open('sample_input.txt')


def dfs(idx, cnt):
    global ans
    is_last = True

    for i in graph[idx]:
        if not visited[i]:
            is_last = False
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

    if is_last and ans < cnt:
        ans = cnt


# main
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = 0

    for i in range(1, N+1):
        visited[i] = True
        dfs(i, 1)
        visited[i] = False

    print('#{} {}'.format(tc, ans))
