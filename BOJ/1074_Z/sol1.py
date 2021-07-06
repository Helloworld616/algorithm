# 시간초과

import sys
sys.stdin = open('input.txt')


def z_move(power, plus, row, col, start):
    if power == 1:
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            start += 1
            if n_row == r and n_col == c-1:
                print(start)
                sys.exit(0)
    else:
        for i in range(4):
            n_row = row + dr[i] * power
            n_col = col + dc[i] * power
            n_start = start + i * plus
            if n_row <= r and n_col <= c-1:
                z_move(power//2, plus//4, n_row, n_col, n_start)


# main
N, r, c = map(int, input().split())

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

z_move(2**(N-1), 4**(N-1), 0, 0, 0)