import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    check = [[0] * 10 for _ in range(10)]
    cnt = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if color == 2 and arr[i][j] == 1 and check[i][j] < 1:
                    cnt += 1
                    check[i][j] += 1
                if color == 1 and arr[i][j] == 2 and check[i][j] < 1:
                    cnt += 1
                    check[i][j] += 1
                arr[i][j] = color

    print('#{} {}'.format(tc, cnt))
