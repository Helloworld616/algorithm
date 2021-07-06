import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0] * (N + 2) for _ in range(N + 2)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            matrix[i][j] = 101

    row = 1
    col = 0
    delta = 1
    number = 1
    while True:
        while matrix[row][col + delta] > number:
            col += delta
            matrix[row][col] = number
            number += 1

        while matrix[row + delta][col] > number:
            row += delta
            matrix[row][col] = number
            number += 1

        cnt = 0
        for k in range(1, N + 1):
            if 101 in matrix[k]:
                cnt += 1
        if cnt == 0:
            break

        delta = 0 - delta

    print("#{}".format(tc))

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            print(matrix[i][j], end=' ')
        print()