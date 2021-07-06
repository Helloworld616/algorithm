import sys
from collections import deque
sys.stdin = open('input.txt')


def bfs(area, N, M):
    if len(area) == 1:
        return 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    candidate = []
    # 벽을 부순 상태에서의 방문과 벽을 부수지 않은 상태에서의 방문을 구분하기 위해서
    # visit를 3차원 배열로 생성
    visit = [[[False, False] for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = True
    visit[0][0][1] = True
    start = (0, 0, 1, True)
    flag = False
    queue = deque()
    queue.append(start)

    while queue:
        spot = queue.popleft()
        for i in range(4):
            row = spot[0] + dr[i]
            col = spot[1] + dc[i]
            if 0 <= row < N and 0 <= col < M:
                # 각 상황에서 방문 검사를 정확히 해주어야 한다. 안 그러면 무한루프 발생!
                # 벽을 부순 상황인 경우 visit[row][col][0]을 검사
                if visit[row][col][0] and spot[3]:
                    continue
                # 벽을 부수지 않은 상황인 경우 visit[row][col][0]을 검사
                if visit[row][col][1] and not spot[3]:
                    continue
                if spot[3]:
                    visit[row][col][0] = True
                else:
                    visit[row][col][1] = True
                if row == N-1 and col == M-1:
                    flag = True
                    candidate.append(spot[2] + 1)
                elif area[row][col] == 1 and spot[3]:
                    dest = (row, col, spot[2] + 1, False)
                    queue.append(dest)
                elif area[row][col] == 0:
                    dest = (row, col, spot[2] + 1, spot[3])
                    queue.append(dest)
    if flag:
        return min(candidate)
    else:
        return -1


# main
N, M = map(int, sys.stdin.readline().split())
area = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs(area, N, M))