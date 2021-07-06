# 교수님 해설 1

import sys
sys.stdin = open("input.txt", encoding='utf8')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = 0

    # 가장자리 미포함
    for y in range(N):
        for x in range(N):
            abs_sum = 0
            for d in range(4):
                center = matrix[y][x]
                test_y = y + dy[d]
                test_x = x + dx[d]
                if 0 <= test_x < N and 0 <= test_y < N:
                    around = matrix[test_y][test_x]
                    abs_sum += abs(center - around)
            total += abs_sum

    print("#{} {}".format(tc, total))