# 라이브 강의 해설

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 2차원 리스트 크기, K: 내가 원하는 길이
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    ans = 0

    for i in range(N):
        cnt = 0
        # 행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] or j == N-1:
                # 벽을 만났을 때 그 동안 쌓아온 cnt 값이 K이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0
        # 열을 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(tc, ans))