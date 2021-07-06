# 실패

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(mirror):
    queue = deque()
    queue.append([start])
    first = True

    # 상하좌우 방향을 저장한 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        spot = queue.popleft()
        row = spot[0][0]
        col = spot[0][1]
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_row < H and 0 <= n_col < W and mirror[n_row][n_col] != -1:
                move = abs(W * dr[i]) + abs(dc[i])

                if first:
                    mirror[n_row][n_col] = 0
                    queue.append([(n_row, n_col), move])

                elif mirror[row][col] <= mirror[n_row][n_col]:
                    if move == spot[1]:
                        mirror[n_row][n_col] = mirror[row][col]
                    else:
                        mirror[n_row][n_col] = mirror[row][col] + 1
                    if (n_row, n_col) != goal:
                        queue.append([(n_row, n_col), move])
        if first:
            first = False

    return mirror[goal[0]][goal[1]]


# main
# 입력 받아 이차원 리스트 생성
W, H = map(int, input().split())
area = [list(input().rstrip()) for _ in range(H)]
mirror = [[10000]*W for _ in range(H)]
first = True

for i in range(H):
    for j in range(W):
        # 시작점과 도착점 저장
        if area[i][j] == 'C' and first:
            start = (i, j)
            mirror[i][j] = 0
            first = False
        elif area[i][j] == 'C' and not first:
            goal = (i, j)
        # 벽의 위치 체크
        if area[i][j] == '*':
            mirror[i][j] = -1

print(bfs(mirror))