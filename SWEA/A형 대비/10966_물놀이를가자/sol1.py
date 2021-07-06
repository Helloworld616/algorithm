# 성공

import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(queue, visit):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]
            if 0 <= row < N and 0 <= col < M and visit[row][col] == -1:
                visit[row][col] = visit[r][c] + 1
                queue.append((row, col))


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    visit = [[-1] * M for _ in range(N)]

    queue = deque()
    # 이 문제는 반드시 입력을 이렇게 받아야 함!
    # 입력에서 시간을 줄여야만 패스할 수 있다.
    for i in range(N):
        beach = input()
        for j in range(M):
            if beach[j] == 'W':
                queue.append((i, j))
                visit[i][j] += 1

    bfs(queue, visit)

    total = 0
    for i in range(N):
        for j in range(M):
            total += visit[i][j]

    print('#{} {}'.format(tc, total))
