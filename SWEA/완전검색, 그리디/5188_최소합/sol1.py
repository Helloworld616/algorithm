# 시간초과

import sys
sys.stdin = open('sample_input.txt')


dr = [1, 0]
dc = [0, 1]


def move(row, col, numbers, result):
    if row == N-1 and col == N-1:
        result.append(sum(numbers))
    else:
        for i in range(2):
            n_row = row + dr[i]
            n_col = col + dc[i]
            if 0 <= n_row < N and 0 <= n_col < N:
                if len(result) == 0 or (len(result) > 0 and sum(numbers) < min(result)):
                    numbers.append(matrix[n_row][n_col])
                    move(n_row, n_col, numbers, result)
                    numbers.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = []
    move(0, 0, [matrix[0][0]], result)
    print('#{} {}'.format(tc, min(result)))
