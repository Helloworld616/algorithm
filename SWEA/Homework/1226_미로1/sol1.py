import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(start, goal, valid, graph, N):
    queue = deque()
    queue.append(start)
    visit = [False] * (N**2)

    while queue:
        idx = queue.popleft()
        if valid[idx] and not visit[idx]:
            visit[idx] = True
            for vertex in graph[idx]:
                if vertex == goal:
                    return 1
                else:
                    queue.append(vertex)

    return 0


for tc in range(1, 11):
    T = int(input())
    N = 16
    maze = [list(map(int, list(input()))) for _ in range(N)]

    graph = [[] for _ in range(N**2)]
    valid = [False] * (N**2)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    idx = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] != 1:
                valid[idx] = True
                if maze[i][j] == 2:
                    start = idx
                if maze[i][j] == 3:
                    goal = idx
                for k in range(4):
                    row = i + dr[k]
                    col = j + dc[k]
                    if 0 <= row < N and 0 <= col < N and maze[row][col] != 1:
                        graph[idx].append(idx + N * dr[k] + dc[k])
            idx += 1

    print('#{} {}'.format(tc, bfs(start, goal, valid, graph, N)))

