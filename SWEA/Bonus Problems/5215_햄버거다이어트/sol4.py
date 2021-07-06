import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())
    val = []
    cal = []

    for _ in range(N):
        v, c = map(int, input().split())
        val.append(v)
        cal.append(c)

    table = [[0] * (L + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, L + 1):
            if cal[i - 1] <= j:
                temp = val[i - 1] + table[i - 1][j - cal[i - 1]]
                if temp > table[i - 1][j]:
                    table[i][j] = temp
                else:
                    table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j]

    print('#{} {}'.format(tc, table[N][L]))