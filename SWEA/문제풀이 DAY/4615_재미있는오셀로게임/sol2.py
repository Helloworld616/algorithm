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

    for _ in range(M):
        row, col, stone = map(int, input().split())
        r = row - 1
        c = col - 1
        board[r][c] = stone


        if stone == 1:
            # 가로 이동
            for i in range(0, c):
                if board[r][i] == 1:
                    idx = i
                    for j in range(idx + 1, c):
                        board[r][i] = 1
                    break

            for i in range(c + 1, N):
                if board[r][i] == 1:
                    idx = i
                    for j in range(c + 1, idx):
                        board[r][i] = 1
                    break
            
            # 세로 이동
            for i in range(0, r):
                if board[i][c] == 1:
                    idx = i
                    for j in range(idx + 1, r):
                        board[i][c] = 1
                    break

            for i in range(r + 1, N):
                if board[i][c] == 1:
                    idx = i
                    for j in range(r + 1, idx):
                        board[i][c] = 1
                    break

            # 대각선 이동 1
            for i in range(1, r + 1):
                if board[r - i][c - i] == 1:
                    idx = i
                    for j in range(i, 0, -1):
                        board[r - j][c - j] = 1
                    break

            inc = 1
            while r + inc < N and c + inc < N:
                if board[r + inc][c + inc] == 1:
                    break
                inc += 1
            for j in range(1, inc):
                board[r + j][c + j] = 1

            # 대각선 이동 2
            inc = 1
            while r + inc < N and c - inc >= 0:
                if board[r + inc][c - inc] == 1:
                    break
                inc += 1
            for j in range(1, inc):
                board[r + j][c - j] = 1

            inc = 1
            while r - inc >= 0  and c + inc < N:
                if board[r - inc][c + inc] == 1:
                    break
                inc += 1
            for j in range(1, inc):
                board[r - j][c + j] = 1

        if stone == 2:
            # 가로 이동
            for i in range(0, c):
                if board[r][i] == 2:
                    idx = i
                    for j in range(idx + 1, c):
                        board[r][i] = 2
                    break

            for i in range(c + 1, N):
                if board[r][i] == 2:
                    idx = i
                    for j in range(c + 1, idx):
                        board[r][i] = 2
                    break

            # 세로 이동
            for i in range(0, r):
                if board[i][c] == 2:
                    idx = i
                    for j in range(idx + 1, r):
                        board[i][c] = 2
                    break

            for i in range(r + 1, N):
                if board[i][c] == 2:
                    idx = i
                    for j in range(r + 1, idx):
                        board[i][c] = 2
                    break

            # 대각선 이동 1
            for i in range(1, r + 1):
                if board[r - i][c - i] == 2:
                    idx = i
                    for j in range(i, 0, -1):
                        board[r - j][c - j] = 2
                    break

            inc = 1
            while r + inc < N and c + inc < N:
                if board[r + inc][c + inc] == 2:
                    break
                inc += 1

            for j in range(1, inc):
                board[r + j][c + j] = 2

            # 대각선 이동 2
            inc = 1
            while r + inc < N and c - inc >= 0:
                if board[r + inc][c - inc] == 2:
                    break
                inc += 1
            for j in range(1, inc):
                board[r + j][c - j] = 2

            inc = 1

            while r - inc >= 0 and c + inc < N:
                if board[r - inc][c + inc] == 2:
                    break
                inc += 1
            for j in range(1, inc):
                board[r - j][c + j] = 2

        for i in range(N):
            print(board[i])
        print()

    white = 0
    black = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                black += 1
            elif board[i][j] == 2:
                white += 1

    print('#{} {} {}'.format(tc, black, white))






