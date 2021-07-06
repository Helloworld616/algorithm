# 실패

import sys
from collections import deque
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(mirror):
    queue = deque()
    queue.append([start])
    visit = [[[False, False, False, False] for _ in range(W)] for _ in range(H)]
    visit[start[0]][start[1]][0] = True
    visit[start[0]][start[1]][1] = True
    visit[start[0]][start[1]][2] = True
    visit[start[0]][start[1]][3] = True
    first = True

    # 상하좌우 방향을 저장한 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        spot = queue.popleft()
        print(spot)
        for i in range(4):
            row = spot[0][0] + dr[i]
            col = spot[0][1] + dc[i]
            if 0 <= row < H and 0 <= col < W and mirror[row][col] != -1:
                move = abs(W * dr[i]) + abs(dc[i])

                if first:
                    mirror[row][col] = 0
                    visit[row][col][i] = True
                    queue.append([(row, col), move, i])

                elif not visit[row][col][spot[2]]:
                    visit[row][col][spot[2]] = True
                    current = mirror[spot[0][0]][spot[0][1]]
                    if move == spot[1] and current <= mirror[row][col]:
                        mirror[row][col] = current
                    elif move != spot[1] and current + 1 <= mirror[row][col]:
                        mirror[row][col] = current + 1
                    if (row, col) != goal:
                        queue.append([(row, col), move, i])
        if first:
            first = False

    pprint(visit)
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
pprint(mirror)