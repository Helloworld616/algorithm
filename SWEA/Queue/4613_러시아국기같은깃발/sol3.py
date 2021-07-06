# 라이브강의 해설

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N행, M열
    flag = [input() for _ in range(N)]

    W = [0] * N
    B = [0] * N
    R = [0] * N
    
    # 행을 보면서 나와 다른 색깔의 개수를를 카운팅
    for i in range(N):
        for j in range(M):
            if flag[i][j] != 'W':
                W[i] += 1
            if flag[i][j] != 'B':
                B[i] += 1
            if flag[i][j] != 'R':
                R[i] += 1

    # 누적시키자.
    for i in range(1, N):
        W[i] += W[i - 1]
        B[i] += B[i - 1]
        R[i] += R[i - 1]

    ans = 987654321
    
    # 각각의 색별로 한줄씩 이상은 확보해야하니까
    for i in range(N-2):
        for j in range(i+1, N-1):
            w_cnt = W[i]
            b_cnt = B[j] - B[i]
            r_cnt = R[N-1] - R[j]

            if ans > w_cnt + b_cnt + r_cnt:
                ans = w_cnt + b_cnt + r_cnt

    print("#{} {}".format(tc, ans))