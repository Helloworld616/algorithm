import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    table = [[0] * (L + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        v, c = map(int, input().split())
        for j in range(1, L + 1):
            if j < c:
                table[i][j] = table[i-1][j]
            else:
                table[i][j] = max(table[i-1][j], table[i-1][j-c] + v)

    print('#{} {}'.format(tc, table[N][L]))