import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(start, goal, maze, visit):
    queue = deque()
    queue.append(start)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        spot = queue.popleft()
        row = spot[0]
        col = spot[1]
        visit[row][col] = True
        for i in range(4):
            new_row = row + dr[i]
            new_col = col + dc[i]
            if 0 <= new_row < N and 0 <= new_col < N and not visit[new_row][new_col]:
                if goal == (new_row, new_col):
                    return maze[row][col]
                maze[new_row][new_col] = maze[row][col] + 1
                queue.append((new_row, new_col))

    return 0


T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visit = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 1:
                visit[i][j] = True
            if maze[i][j] == 2:
                start = (i, j)
                maze[i][j] = 0
            if maze[i][j] == 3:
                goal = (i, j)
                maze[i][j] = 0

    print('#{} {}'.format(tc, bfs(start, goal, maze, visit)))
