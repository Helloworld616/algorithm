# 오답

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    diagonal = [
        [[-1, -1], [-1, 1]],
        [[1, -1], [1, 1]],
        [[-1, -1], [1, -1]],
        [[-1, 1], [1, 1]]
    ]

    visited = [[[False, False] for _ in range(W)] for _ in range(H)]
    visited[0][0][0] = True
    visited[0][0][1] = True
    ans = 40000

    queue = deque()
    queue.append([[0, 0], 0, K])

    while queue:
        spot = queue.popleft()
        row = spot[0][0]
        col = spot[0][1]
        move = spot[1]
        remain = spot[2]
        if row == H-1 and col == W-1 and ans > move:
            print(row, col)
            ans = move

        if move < ans:
            for i in range(4):
                n_row = row + dr[i]
                n_col = col + dc[i]
                if 0 <= n_row < H and 0 <= n_col < W:
                    print(row, col, n_row, n_col, visited[n_row][n_col][0])
                    if area[n_row][n_col] != 1 and not visited[n_row][n_col][0]:
                        visited[n_row][n_col][0] = True
                        queue.append([[n_row, n_col], move + 1, remain])
                    if remain > 0:
                        for j in range(2):
                            h_row = n_row + diagonal[i][j][0]
                            h_col = n_col + diagonal[i][j][1]
                            if 0 <= h_row < H and 0 <= h_col < W and area[h_row][h_col] != 1:
                                if not visited[h_row][h_col][1]:
                                    visited[h_row][h_col][1] = True
                                    queue.append([[h_row, h_col], move + 1, remain - 1])
    print(visited)
    if ans == 40000:
        return -1
    else:
        return ans

# main
K = int(input())
W, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(H)]
print(bfs())