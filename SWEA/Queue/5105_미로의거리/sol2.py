import sys
sys.stdin = open('sample_input.txt')


# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 시작 정점을 찾는 함수
def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


def BFS(r, c):
    # 선형큐를 이용해서 작성을 해보자
    Q = [0] * 1000000
    front = -1
    rear = 0
    Q[rear] = (r, c)

    dist = [[-1] * N for _ in range(N)]
    dist[r][c] = 0

    # 선형큐에서의 공백 검사
    while front != rear:
        front += 1
        curr_r, curr_c = Q[front]
        if maze[curr_r][curr_c] == '3':
            return dist[curr_r][curr_c] - 1
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # 벽으로 둘러싸지 않았기 때문에 범위 검사를 해야 한다.
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue

            # 벽이 아니면서, 거리를 갱신하지 않았다면 좌표를 넣고 갱신
            if maze[nr][nc] != '1' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[curr_r][curr_c] + 1
                rear += 1
                Q[rear] = (nr, nc)

    return 0


T = int(input())


for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    stR, stC = search()
