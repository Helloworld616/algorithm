# 재귀로 풀어서 Stack Overflow 발생!

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def makeNormalGraph():
    graph = [[] for _ in range(N*N)]

    idx = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N and grid[i][j] == grid[row][col]:
                    graph[idx].append(idx + N*dr[k] + dc[k])
            idx += 1

    return graph


def makeBlindGraph():
    graph = [[] for _ in range(N*N)]

    idx = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N:
                    if grid[i][j] == 'R' or grid[i][j] == 'G':
                        if grid[row][col] == 'R' or grid[row][col] == 'G':
                            graph[idx].append(idx + N*dr[k] + dc[k])
                    else:
                        if grid[i][j] == grid[row][col]:
                            graph[idx].append(idx + N*dr[k] + dc[k])
            idx += 1

    return graph


def dfs(idx, graph, visited):
    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, graph, visited)


# main
N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n_graph = makeNormalGraph()
n_visited = [False] * (N*N)
n_district = 0
for i in range(N*N):
    if not n_visited[i] and len(n_graph[i]) > 0:
        dfs(i, n_graph, n_visited)
        n_district += 1

b_graph = makeBlindGraph()
b_visited = [False] * (N*N)
b_district = 0
for i in range(N*N):
    if not b_visited[i] and len(b_graph[i]) > 0:
        dfs(i, b_graph, b_visited)
        b_district += 1

print(n_district, b_district)