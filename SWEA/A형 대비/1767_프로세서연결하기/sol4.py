# 성공
# 시간 : 1207ms

import sys
sys.stdin = open('sample_input.txt')


def charge(cnt, max_cnt, idx, length, record, result):
    if idx == len(cores):
        if cnt > max_cnt[0]:
            max_cnt[0] = cnt
        result.append((cnt, length))
    else:
        if cnt + len(cores) - idx >= max_cnt[0]:
            charge(cnt, max_cnt, idx + 1, length, record, result)
            for i in range(4):
                if checks[idx][i]:
                    row = cores[idx][0] + dr[i]
                    col = cores[idx][1] + dc[i]
                    ltemp = 0
                    rtemp = []
                    while 0 <= row < N and 0 <= col < N and (row, col) not in set(record):
                        ltemp += 1
                        rtemp.append((row, col))
                        row += dr[i]
                        col += dc[i]
                    if row < 0 or col < 0 or row == N or col == N:
                        charge(cnt + 1, max_cnt, idx + 1, length + ltemp, record + rtemp, result)


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if matrix[i][j] == 1:
                cores.append((i, j))

    checks = []

    for core in cores:
        check = []
        for i in range(4):
            row = core[0] + dr[i]
            col = core[1] + dc[i]
            while 0 <= row < N and 0 <= col < N and matrix[row][col] == 0:
                row += dr[i]
                col += dc[i]
            if row < 0 or col < 0 or row == N or col == N:
                check.append(True)
            else:
                check.append(False)
        checks.append(check)

    max_cnt = [0]
    result = []
    charge(0, max_cnt, 0, 0, [], result)

    answer = []
    for ans in result:
        if ans[0] == max_cnt[0]:
            answer.append(ans[1])

    print('#{} {}'.format(tc, min(answer)))

