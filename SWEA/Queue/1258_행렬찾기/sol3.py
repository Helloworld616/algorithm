for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                r, c, = i, j
                # 범위를 앞에 위치
                while r < N and arr[r][j] != 0:
                    r += 1
                while c < N and arr[i][c] != 0:
                    c += 1

                ans.append([r-i, c-j])
                
                # 초기화하는 작업
                for a in range(i, r):
                    for b in range(j, c):
                        arr[a][b] = 0
    ans.sort(key = lambda x : (x[0] * x[1], x[0]))
    for i in range(len(ans)):
        print("#{} {}".format(ans[i][0], ans[i][1]), end = ' ')
    print()