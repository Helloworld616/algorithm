import sys
from collections import deque
sys.stdin = open('input.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(row, col, visited):
    queue = deque()
    queue.append((row, col))

    value = rooms[row][col]
    move = 0
    visited[row][col] = 1

    while queue:
        info = queue.popleft()
        row = info[0]
        col = info[1]
        is_end = True

        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_row < N and 0 <= n_col < N and rooms[n_row][n_col] == rooms[row][col] + 1\
                    and visited[n_row][n_col] < visited[row][col] + 1:
                is_end = False
                visited[n_row][n_col] = visited[row][col] + 1
                queue.append((n_row, n_col))

        if is_end and visited[row][col] > move:
            move = visited[row][col]
            if rooms[row][col] < value:
                value = rooms[row][col]

    return value, move


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    value_result = 0
    move_result = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                value_now, move_now = bfs(i, j, visited)
                if move_now > move_result:
                    value_result = value_now
                    move_result = move_now
                elif move_now == move_result and value_now < value_result:
                    value_result = value_now

    print('#{} {} {}'.format(tc, value_result, move_result))
