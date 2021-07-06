import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[1] * N for _ in range(N)]
    if N > 1:
        length = N-1
        row = 0
        col = 0
        number = 1
        flag = True
        while flag:
            for i in range(length):
                matrix[row][col] = number
                if number == N ** 2:
                    flag = False
                    break
                col += 1
                number += 1

            for i in range(length):
                matrix[row][col] = number
                if number == N ** 2:
                    flag = False
                    break
                row += 1
                number += 1

            for i in range(length):
                matrix[row][col] = number
                if number == N ** 2:
                    flag = False
                    break
                col -= 1
                number += 1

            for i in range(length):
                matrix[row][col] = number
                if number == N ** 2:
                    flag = False
                    break
                if i == length-1:
                    col += 1
                else:
                    row -= 1
                number += 1

            if length > 2:
                length -= 2
            else:
                length -= 1

    print("#{}".format(tc))

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end = ' ')
        print()
