import sys
sys.stdin = open('input.txt')


def solution(sdoku):
    for i in range(9):
        if len(set(sdoku[i])) != 9:
            return 0

    for i in range(9):
        check = []
        for j in range(9):
            check.append(sdoku[j][i])
        if len(set(check)) != 9:
            return 0

    row = 0
    start = 0
    while row < 9:
        check2 = [0] * 10
        for j in range(row, row + 3):
            for k in range(start, start + 3):
                check2[sdoku[j][k]] += 1
        for idx in range(1, len(check2)):
            if check2[idx] != 1:
                return 0

        start += 3

        if start >= 9:
            row += 3
            start = 0

    return 1


T = int(input())

for tc in range(1, T + 1):
    sdoku = []
    for i in range(9):
        row = list(map(int, input().split()))
        sdoku.append(row)
    print('#{} {}'.format(tc, solution(sdoku)))



