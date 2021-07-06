# 시간초과

from collections import deque


def solution(board):
    N = len(board)
    INF = float('inf')

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cost = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, -1, 'start'))
    cost[0][0][0] = 0
    board[0][0] = 1

    while queue:
        spot = queue.popleft()
        row = spot[0]
        col = spot[1]
        state = spot[2]
        previous = spot[3]

        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_row < N and 0 <= n_col < N and board[n_row][n_col] != 1:
                next_dr = 'vertical' if i < 2 else 'horizon'
                if previous == 'start':
                    cost[n_row][n_col][i] = cost[row][col][0] + 100
                    queue.append((n_row, n_col, i, next_dr))
                else:
                    new_cost = cost[row][col][state] + 100 if previous == next_dr else cost[row][col][state] + 600
                    if new_cost <= cost[n_row][n_col][i]:
                        cost[n_row][n_col][i] = new_cost
                        if n_row != (N - 1) or n_col != (N - 1):
                            queue.append((n_row, n_col, i, next_dr))

    return min(cost[N-1][N-1])


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
