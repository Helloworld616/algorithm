# PASS

from collections import deque


# bfs 함수
def bfs(board, row, col, dir):
    # 보드의 길이 저장
    N = len(board)

    # 상하좌우 4방향 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 비용을 저장하는 이차원 리스트 생성 및 초기화
    cost = [[float('inf')] * N for _ in range(N)]

    # 큐 생성 및 시작점 담기
    queue = deque()
    # 행, 열, 비용, 방향을 담는다.
    queue.append((row, col, 100, dir))
    # 비용 저장
    cost[row][col] = 100

    # bfs 실시
    while queue:
        # 위치 정보 가져오기
        spot = queue.popleft()
        row = spot[0]  # 행
        col = spot[1]  # 열
        now_cost = spot[2]  # 현재까지 쌓인 비용
        previous = spot[3]  # 이전의 방향

        # 4방향 탐색
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            # 새로운 방향이 보드 범위 안에 있고, 갈 수 있는 지점일 경우
            if 0 <= n_row < N and 0 <= n_col < N and board[n_row][n_col] != 1:
                # 방향 체크
                # 이전과 같은 방향이라면 비용에 100을 더하고, 다른 방향이라면 600을 더한다!
                # 지나쳐 온 곳의 비용은 필연적으로 현재 비용보다 작으므로 걸러짐
                new_cost = now_cost + 100 if previous == i else now_cost + 600
                # 새로운 비용이 기존의 비용 이하일 경우
                if new_cost <= cost[n_row][n_col]:
                    # 비용을 갱신하고 다음 탐색을 위해 정보를 큐에 담는다.
                    cost[n_row][n_col] = new_cost
                    queue.append((n_row, n_col, new_cost, i))

    # 도착지의 비용 반환
    return cost[N-1][N-1]


# 정답 함수
def solution(board):
    # 두 방향 탐색 결과를 무한으로 초기화
    first_result = float('inf')
    second_result = float('inf')
    # 시작점으로 다시 돌아오지 않도록 전처리
    board[0][0] = 1

    # 오른쪽 방향이 뚫려 있을 경우, 오른쪽 bfs 실시
    if board[0][1] == 0:
        first_result = bfs(board, 0, 1, 3)
    # 아래쪽 방향이 뚫려 있을 경우, 아래쪽 bfs 실시
    if board[1][0] == 0:
        second_result = bfs(board, 1, 0, 1)

    # 두 가지 탐색 결과 중 최솟값을 반환
    return min(first_result, second_result)


print(solution([[0,0,0],[0,0,1],[1,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
print(solution([[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0]]))

print(solution([[0,0,0,0,0],[0,1,1,1,0],[0,0,1,0,0],[1,0,0,0,1], [0,1,1,0,0]]))
