# 실패

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    #print(board)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[N//2 - 1][N//2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2
    for i in range(M):
        row, col, stone = map(int, input().split())
        r = row - 1
        c = col - 1
        board[r][c] = stone
        print(board)
        if stone == 1:
            for direction in directions:
                if 0 <= r + 2 * direction[0] < N and 0 <= c + 2 * direction[1] < N:
                    if board[r + direction[0]][c + direction[1]] == 2 and board[r + 2 * direction[0]][c + 2 * direction[1]] == 1:
                        board[r + direction[0]][c + direction[1]] = 1

        elif stone == 2:
            for direction in directions:
                if 0 <= r + 2 * direction[0] < N and 0 <= c + 2 * direction[1] < N:
                    if board[r + direction[0]][c + direction[1]] == 1 and board[r + 2 * direction[0]][c + 2 * direction[1]] == 2:
                        board[r + direction[0]][c + direction[1]] = 2

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))






