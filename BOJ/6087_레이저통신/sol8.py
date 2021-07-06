import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


def bfs(mirror):
    queue = deque()

    # 상하좌우 방향을 저장한 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        mirror[start[0]][start[1]][i] = 0
        # 위치, 방향, 거울 갯수, 저장 위치
        queue.append([start, i, 0, i])

    while queue:
        spot = queue.popleft()

        row = spot[0][0]
        col = spot[0][1]
        n_row = row + dr[spot[1]]
        n_col = col + dc[spot[1]]

        while 0 <= n_row < H and 0 <= n_col < W and area[n_row][n_col] != '*' and mirror[n_row][n_col][spot[3]] == 10000:
            mirror[n_row][n_col][spot[3]] = spot[2]
            if (n_row, n_col) != goal:
                for i in range(4):
                    if i == spot[1]:
                        continue
                    m_row = n_row + dr[i]
                    m_col = n_col + dc[i]
                    if 0 <= m_row < H and 0 <= m_col < W and area[m_row][m_col] != '*' and mirror[m_row][m_col][spot[3]] == 10000:
                        mirror[m_row][m_col][spot[3]] = mirror[n_row][n_col][spot[3]] + 1
                        if (m_row, m_col) != goal:
                            queue.append([(m_row, m_col), i, mirror[m_row][m_col][spot[3]], spot[3]])
                n_row += dr[spot[1]]
                n_col += dc[spot[1]]

    print(mirror)
    return min(mirror[goal[0]][goal[1]])


# main
# 입력 받아 이차원 리스트 생성
W, H = map(int, input().split())
area = [list(input().rstrip()) for _ in range(H)]
mirror = [[[10000]*4 for _ in range(W)] for _ in range(H)]
first = True

for i in range(H):
    for j in range(W):
        # 시작점과 도착점 저장
        if area[i][j] == 'C' and first:
            start = (i, j)
            first = False
        elif area[i][j] == 'C' and not first:
            goal = (i, j)

print(bfs(mirror))