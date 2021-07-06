import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(visit):
    queue = deque()
    queue.append((R, C))

    while queue:
        spot = queue.popleft()

        r = spot[0]
        c = spot[1]

        for i in range(4):
            row = r + dr[i]
            col = c + dc[i]
            if 0 <= row < N and 0 <= col < M and not visit[row][col] and tunnel[row][col] > 0:
                if pipe[tunnel[row][col]][(i+2) % 4] == -1 or pipe[tunnel[r][c]][i] == -1:
                    continue
                if pipe[tunnel[row][col]][(i+2) % 4] == (pipe[tunnel[r][c]][i] + 2) % 4:
                    queue.append((row, col))
                    visit[row][col] = visit[r][c] + 1


T = int(input())
pipe = [[], [0, 1, 2, 3], [0, -1, 2, -1], [-1, 1, -1, 3], [0, 1, -1, -1], [-1, 1, 2, -1], [-1, -1, 2, 3], [0, -1, -1, 3]]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for tc in range(1, T+1):
    info = list(map(int, input().split()))

    N = info[0]
    M = info[1]
    R = info[2]
    C = info[3]
    L = info[4]

    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = 1

    bfs(visit)
    answer = 0
    for i in range(N):
        for j in range(M):
            if 0 < visit[i][j] <= L:
                answer += 1

    print('#{} {}'.format(tc, answer))
