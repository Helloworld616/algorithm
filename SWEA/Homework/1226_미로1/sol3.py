import sys

sys.stdin = open('input.txt')

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    global flag

    # 도착지점 확인
    if maze[r][c] == 3:
        flag = 1
        return

    maze[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            DFS(nr, nc)


for tc in range(10):
    tc_num = int(input())
    N = 16

    maze = [list(map(int, input())) for _ in range(N)]

    # 시작점을 찾아서 출발해야하므로
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1

    flag = 0 # 0으로 초기화
    DFS(sR, sC)
    print('#{} {}'.format(tc_num, flag))