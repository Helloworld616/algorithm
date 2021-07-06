# 시간초과

import sys
from collections import deque
sys.stdin = open('input.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, 1, 1]


def bfs(row, col):
    queue = deque()
    queue.append((row, col, 1))
    value = rooms[row][col]
    move = 0

    while queue:
        info = queue.popleft()
        row = info[0]
        col = info[1]
        cnt = info[2]
        is_end = True

        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_row < N and 0 <= n_col < N and rooms[n_row][n_col] == rooms[row][col] + 1:
                is_end = False
                queue.append((n_row, n_col, cnt + 1))

        if is_end and cnt > move:
            move = cnt

    return value, move


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    value_result = 0
    move_result = 0
    for i in range(N):
        for j in range(N):
            value_now, move_now = bfs(i, j)
            if move_now > move_result:
                value_result = value_now
                move_result = move_now
            elif move_now == move_result and value_now < value_result:
                value_result = value_now

    print(value_result, move_result)


