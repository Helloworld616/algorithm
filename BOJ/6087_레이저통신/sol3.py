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
        for i in range(4):
            row = spot[0][0] + dr[i]
            col = spot[0][1] + dc[i]
            if 0 <= row < H and 0 <= col < W and mirror[row][col] != -1:
                move = abs(W * dr[i]) + abs(dc[i])
                if first:
                    mirror[row][col] = 0
                    queue.append([(row, col), move])
                elif mirror[spot[0][0]][spot[0][1]] <= mirror[row][col]:
                    if move == spot[1]:
                        mirror[row][col] = mirror[spot[0][0]][spot[0][1]]
                    else:
                        mirror[row][col] = mirror[spot[0][0]][spot[0][1]] + 1
                    if (row, col) != goal:
                        queue.append([(row, col), move])
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
            first = False
        elif area[i][j] == 'C' and not first:
            goal = (i, j)
        # 벽의 위치 체크
        if area[i][j] == '*':
            mirror[i][j] = -1

print(bfs(mirror))