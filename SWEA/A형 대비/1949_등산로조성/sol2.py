# 성공

import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def dfs(spot, mountain, visit, result):
    # spot의 원소들을 하나씩 꺼내서 변수에 할당
    row = spot[0]
    col = spot[1]
    road = spot[2]
    cut = spot[3]

    # 방문 체크
    flag = True

    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]
        if 0 <= n_row < N and 0 <= n_col < N and not visit[n_row][n_col]:
            if mountain[n_row][n_col] < mountain[row][col]:
                flag = False
                visit[row][col] = True
                dfs((n_row, n_col, road+1, cut), mountain, visit, result)
                visit[row][col] = False
            else:
                if not cut:
                    cutting = 0
                    for k in range(1, K+1):
                        if mountain[n_row][n_col] - k < mountain[row][col]:
                            cutting = k
                            break
                    if cutting != 0:
                        flag = False
                        mountain[n_row][n_col] -= k
                        visit[row][col] = True
                        dfs((n_row, n_col, road + 1, True), mountain, visit, result)
                        visit[row][col] = False
                        mountain[n_row][n_col] += k

    if flag:
        result.append(road)


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
                start.append((i, j, 1, False))

    final = []
    length = len(start)
    for i in range(length):
        spot = start.popleft()
        visit = [[False]*N for _ in range(N)]
        result = []
        visit[spot[0]][spot[1]] = True
        dfs(spot, mountain, visit, result)
        visit[spot[0]][spot[1]] = False
        final += result

    print('#{} {}'.format(tc, max(final)))