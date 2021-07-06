import sys
sys.stdin = open("input.txt")

T = 10


def solution(N, matrix):
    maximum = 0
    row_total = col_total = x1_total = x2_total = 0
    for idx in range(N):
        x1_total += matrix[idx][idx]
        x2_total += matrix[idx][N-1-idx]
        for jdx in range(N):
            row_total += matrix[idx][jdx]
            col_total += matrix[jdx][idx]
        if row_total > maximum:
            maximum = row_total
        if col_total > maximum:
            maximum = col_total
        row_total = col_total = 0

    if x1_total > maximum:
        maximum = x1_total

    if x2_total > maximum:
        maximum = x2_total

    return maximum


for _ in range(1, T+1):
    tc = input()
    N = 100
    matrix = [
        list(map(int, input().split())) for _ in range(N)
    ]
    print('#{} {}'.format(tc, solution(N, matrix)))