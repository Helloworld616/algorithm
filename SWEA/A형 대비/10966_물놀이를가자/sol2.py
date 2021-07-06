# 시간초과

import sys
sys.stdin = open('sample_input.txt')


def bfs(beach):
    queue = []
    for i in range(len(water)):
        queue.append(water[i])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visit = [[False] * M for _ in range(N)]

    while queue:
        spot = queue.pop(0)
        visit[spot[0]][spot[1]] = True
        for i in range(4):
            row = spot[0] + dr[i]
            col = spot[1] + dc[i]
            if 0 <= row < N and 0 <= col < M and beach[row][col] == 'L' and not visit[row][col]:
                visit[row][col] = True
                beach[row][col] = beach[spot[0]][spot[1]] + 1
                queue.append((row, col))


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    beach = [list(input()) for _ in range(N)]
    water = []

    for i in range(N):
        for j in range(M):
            if beach[i][j] == 'W':
                beach[i][j] = 0
                water.append((i, j))

    bfs(beach)

    total = 0
    for i in range(N):
        for j in range(M):
            total += beach[i][j]

    print('#{} {}'.format(tc, total))


