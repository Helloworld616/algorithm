import sys
sys.stdin = open("sample_input.txt")
from collections import deque


def bfs(apart, humans):
    dh = [-1, 1, 0, 0, 0, 0]
    dn = [0, 0, -1, 1, 0, 0]
    dm = [0, 0, 0, 0, -1, 1]

    while humans:
        h, n, m = humans.popleft()
        for i in range(6):
            nh = h + dh[i]
            nn = n + dn[i]
            nm = m + dm[i]
            if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and apart[nh][nn][nm] == -1:
                apart[nh][nn][nm] = apart[h][n][m] + 1
                humans.append((nh, nn, nm))


def is_remain():
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if apart[i][j][k] == -1:
                    return True

    return False


# main
T = int(input())

for tc in range(1, T+1):
    M, N, H = map(int, input().split())
    apart = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
    humans = deque()
    zombies = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if apart[i][j][k] == 1:
                    humans.append((i, j, k))
                if apart[i][j][k] == -1:
                    zombies += 1

    if not len(humans):
        print("#{} {}".format(tc, 'STILL ZOMBIES'))
    elif not zombies:
        print("#{} {}".format(tc, 'ALL HUMANS'))
    else:
        bfs(apart, humans)
        if is_remain():
            print("#{} {}".format(tc, 'STILL ZOMBIES'))
        else:
            ans = 0
            for i in range(H):
                for j in range(N):
                    compare = max(apart[i][j])
                    if compare > ans:
                        ans = compare
            print("#{} {}".format(tc, ans - 1))

