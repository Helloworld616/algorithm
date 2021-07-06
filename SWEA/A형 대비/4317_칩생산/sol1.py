# 오답

import sys
sys.stdin = open("sample_sample_input.txt")


dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]


def find_location(location):
    cnt = 0

    for i in range(H-1):
        for j in range(W-1):
            is_available = True

            for k in range(4):
                if matrix[i + dr[k]][j + dc[k]]:
                    is_available = False
                    break

            if is_available:
                location.append((i, j))
                cnt += 1

    return cnt


def cal(dp, location, record):
    for i in range(len(location)):
        for j in range(i, -1, -1):
            if abs(location[i][0] - location[j][0]) <= 1 and abs(location[i][1] - location[j][1]) <= 1:
                continue

            record[i].append((location[j][0], location[j][1]))

            for row, col in record[j]:
                if abs(location[i][0] - row) <= 1 and abs(location[i][1] - col) <= 1:
                    continue
                record[i].append((row, col))

            break
        dp[i] = len(record[i]) + 1


# main
T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(H)]
    location = []

    cnt = find_location(location)
    dp = [0] * cnt
    record = [[] for _ in range(cnt)]

    # print(cnt, location)
    # print(dp)
    ans = cal(dp, location, record)
    print(location)
    print(dp)
    print(record)
    print()


    # print("#{} {}".format(tc, ans))

