# 교수님 해설 2

import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = []
    matrix.append([0] * (N+2))
    for _ in range(N):
        matrix.append(
           [0, *map(int, input().split()), 0]
        )
    matrix.append([0] * (N + 2))

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = 0

    # 가장자리 미포함
    for y in range(1, N+1):  # 1, 2, 3, 4, 5 ... N
        for x in range(1, N+1):
            abs_sum = 0
            for d in range(4):
                center = matrix[y][x]
                test_y = y + dy[d]
                test_x = x + dx[d]
                around = matrix[test_y][test_x]
                if around:
                    abs_sum += abs(center - around)
            total += abs_sum

    print("#{} {}".format(tc, total))
