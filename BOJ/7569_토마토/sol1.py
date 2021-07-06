import sys
from collections import deque
sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(matrix, q):
    dh = [0, 0, 0, 0, -1, 1]
    dr = [-1, 1, 0, 0, 0, 0]
    dc = [0, 0, -1, 1, 0, 0]

    while q:
        height, row, col = q.popleft()

        for i in range(6):
            n_height = height + dh[i]
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_height < H and 0 <= n_row < N and 0 <= n_col < M and not matrix[n_height][n_row][n_col]:
                matrix[n_height][n_row][n_col] = matrix[height][row][col] + 1
                queue.append((n_height, n_row, n_col))

    return matrix


def cal():
    days = 0
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if not result[i][j][k]:
                    return 0
                if result[i][j][k] > days:
                    days = result[i][j][k]
    return days


# main
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

result = bfs(box, queue)
print(cal() - 1)

