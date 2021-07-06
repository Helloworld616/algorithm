# 실패

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(area):
    queue = deque()
    queue.append([start])
    visit = [[[False, False, False, False] for _ in range(W)] for _ in range(H)]
    visit[start[0]][start[1]][0] = True
    visit[start[0]][start[1]][1] = True
    visit[start[0]][start[1]][2] = True
    visit[start[0]][start[1]][3] = True
    first = True
    result = []

    # 상하좌우 방향을 저장한 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        spot = queue.popleft()
        print(spot)
        for i in range(4):
            row = spot[0][0] + dr[i]
            col = spot[0][1] + dc[i]
            if 0 <= row < H and 0 <= col < W and area[row][col] != '*':
                move = abs(W * dr[i]) + abs(dc[i])
                if first:
                    if (row, col) == goal:
                        return 0
                    visit[row][col][i] = True
                    queue.append([(row, col), move, i, 0])

                elif not visit[row][col][spot[2]]:
                    visit[row][col][spot[2]] = True
                    if move == spot[1]:
                        mirror = spot[3]
                    elif move != spot[1]:
                        mirror = spot[3] + 1
                    if (row, col) != goal:
                        queue.append([(row, col), move, i, mirror])
                    else:
                        result.append(mirror)
        if first:
            first = False

    return min(result)


# main
# 입력 받아 이차원 리스트 생성
W, H = map(int, input().split())
area = [list(input().rstrip()) for _ in range(H)]
first = True

for i in range(H):
    for j in range(W):
        # 시작점과 도착점 저장
        if area[i][j] == 'C' and first:
            start = (i, j)
            first = False
        elif area[i][j] == 'C' and not first:
            goal = (i, j)


print(bfs(area))