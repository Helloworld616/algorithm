# 성공

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[N//2 - 1][N//2 - 1] = 2
    board[N // 2 - 1][N // 2] = 1
    board[N // 2][N // 2 - 1] = 1
    board[N // 2][N // 2] = 2

    for _ in range(M):
        row, col, stone = map(int, input().split())
        r = row - 1
        c = col - 1
        board[r][c] = stone

        if stone == 1:
            myself = 1
            change = 2
        else:
            myself = 2
            change = 1

        for direction in directions:
            n = 1
            idx = []
            while 0 <= r + n * direction[0] < N and 0 <= c + n * direction[1] < N:
                if board[r + n * direction[0]][c + n * direction[1]] == 0:
                    break
                if board[r + n * direction[0]][c + n * direction[1]] == change:
                    idx.append((r + n * direction[0], c + n * direction[1]))
                if board[r + n * direction[0]][c + n * direction[1]] == myself:
                    for i in idx:
                        board[i[0]][i[1]] = myself
                    break
                n += 1

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))