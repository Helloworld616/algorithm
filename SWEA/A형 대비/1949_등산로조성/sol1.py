# 오답

import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(mountain, start):
    length = len(start)
    result = []

    for _ in range(length):
        location = start.popleft()
        visit = [[[False, False] for _ in range(N)] for _ in range(N)]
        visit[location[0]][location[1]][0] = True
        visit[location[0]][location[1]][1] = True
        queue = deque()
        queue.append(location)
        change = (10, 10)
        cut = 0

        while queue:
            spot = queue.popleft()
            row = spot[0]
            col = spot[1]
            road = spot[2]
            chance = spot[3]

            flag = True
            for i in range(4):
                n_row = row + dr[i]
                n_col = col + dc[i]
                if 0 <= n_row < N and 0 <= n_col < N:
                    if mountain[row][col] > mountain[n_row][n_col]:
                        if not visit[n_row][n_col][0] and chance:
                            flag = False
                            visit[n_row][n_col][0] = True
                            queue.append((n_row, n_col, road + 1, chance))
                        elif not visit[n_row][n_col][1] and not chance:
                            flag = False
                            visit[n_row][n_col][1] = True
                            queue.append((n_row, n_col, road + 1, chance))
                    else:
                        if not visit[n_row][n_col][1] and chance:
                            flag = False
                            visit[n_row][n_col][1] = True
                            chance = False
                            for i in range(1, K+1):
                                mountain[n_row][n_col] -= i
                                if mountain[n_row][n_col] < mountain[row][col]:
                                    cut = i
                                    break
                                mountain[n_row][n_col] += i

                            change = (n_row, n_col)
                            queue.append((n_row, n_col, road + 1, chance))
            if flag:
                result.append(road)

        if change != (10, 10):
            mountain[change[0]][change[1]] += cut

    return max(result)



T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_num = mountain[0][0]
    for i in range(N):
        for j in range(N):
            if mountain[i][j] > max_num:
                max_num = mountain[i][j]

    start = deque()
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_num:
                start.append((i, j, 1, True))

    print('#{} {}'.format(tc, bfs(mountain, start)))
