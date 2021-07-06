import sys
# from pandas import Dataframe
sys.stdin = open("sample_input.txt")


def solution(N, matrix, start, goal):
    visited = [[False for _ in range(N)] for _ in range(N)]
    # found = False

    # print(DataFrame(visited))
    def dfs(x, y):
        # nonlocal found
        if matrix[y][x] == 3:
            # found = True
            print('Found!')
        else:
            dys = [-1, 1, 0, 0]
            dxs = [0, 0, -1, 1]
            for idx in range(4):
                dy, dx = dys[idx], dxs[idx]
                # 1. 이동하려는 좌표값이 0 <= x, y, < N을 만족하는지
                # x + dx / y + dy
                if 0 <= x + dx < N and 0 <= y + dy < N:
                    # 2. 벽이 아닌가(길, 목적지, 출발지)
                    if matrix[y + dy][x + dx] != 1:
                        # 3. 방문했는지...?
                        if not visited[y + dy][x + dx]:
                            dfs(x+dx, y+dy)
    dfs(*start)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input())) for _ in range(N))]
    for y in range(N):
        for x in range(N):
            if matrix[y][x] == 2:
                start = (x, y)
            elif matrix[y][x] == 3:
                goal = (x, y)


    print("{} {}".format(tc, solution(N, matrix, start, goal)))