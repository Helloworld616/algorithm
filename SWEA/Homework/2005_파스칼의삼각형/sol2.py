# 교수님 해설

import sys
sys.stdin = open('input.txt')


def solution(N):
    matrix = [[] for _ in range(N)]
    for row in range(N):
        cnt = row + 1 # row_idx + 1이 요소 개수
        for col in range(cnt):
            if col == 0 or col == row:
                matrix[row].append(1)
            else:
                upper_row = matrix[row-1]
                val = upper_row[col] + upper_row[col]
                matrix[row].append(val)

    return [map(str, row) for row in matrix]
        


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    print(solution(N))
    # for s in solution(N):
