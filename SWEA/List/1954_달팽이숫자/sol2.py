import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * N for _ in range(N)]

    row = 0
    col = -1
    delta = 1
    number = 1
    length = N
    while True:
        for i in range(length):
            col += delta
            matrix[row][col] = number
            number += 1

        length -= 1

        if length < 0:
            break

        for j in range(length):
            row += delta
            matrix[row][col] = number
            number += 1

        delta = 0 - delta

    print("#{}".format(tc))

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=' ')
        print()