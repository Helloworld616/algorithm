import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    check = [False] * (N*N + 1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N and rooms[row][col] == rooms[i][j] + 1:
                    check[rooms[i][j]] = True
                    break

    start = 0
    cnt = 0
    ans = [0, 0]

    for i in range(1, N*N+1):
        if check[i]:
            if not cnt:
                start = i
            cnt += 1
        else:
            if cnt > ans[1]:
                ans[0] = start
                ans[1] = cnt
            elif cnt == ans[1] and start < ans[0]:
                ans[0] = start
            cnt = 0

    print('#{} {} {}'.format(tc, ans[0], ans[1]+1))
