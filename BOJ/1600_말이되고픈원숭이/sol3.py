import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    diar = [-2, -2, 2, 2, -1, 1, -1, 1]
    diac = [-1, 1, -1, 1, -2, -2, 2, 2]

    visited = [[[False] * (K+1) for _ in range(W)] for _ in range(H)]
    for i in range(K+1):
        visited[0][0][i] = True

    ans = 40000

    queue = deque()
    queue.append([[0, 0], 0, 0])

    while queue:
        spot = queue.popleft()
        row = spot[0][0]
        col = spot[0][1]
        move = spot[1]
        used = spot[2]

        if row == H-1 and col == W-1 and ans > move:
            ans = move

        if move < ans:
            if used < K:
                for i in range(8):
                    h_row = row + diar[i]
                    h_col = col + diac[i]
                    if 0 <= h_row < H and 0 <= h_col < W and area[h_row][h_col] != 1:
                        if not visited[h_row][h_col][used + 1]:
                            visited[h_row][h_col][used + 1] = True
                            queue.append([[h_row, h_col], move + 1, used + 1])

            for i in range(4):
                n_row = row + dr[i]
                n_col = col + dc[i]
                if 0 <= n_row < H and 0 <= n_col < W:
                    if area[n_row][n_col] != 1 and not visited[n_row][n_col][used]:
                        visited[n_row][n_col][used] = True
                        queue.append([[n_row, n_col], move + 1, used])

    if ans == 40000:
        return -1
    else:
        return ans

# main
K = int(input())
W, H = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(H)]
print(bfs())