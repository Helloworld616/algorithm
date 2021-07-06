import sys
sys.stdin = open('sample_input.txt')


def cal(menu, record, result, idx):
    if len(record) == N//2:
        remain = []
        for i in range(N):
            if i not in set(record):
                remain.append(i)

        total1 = 0
        for i in range(len(record)-1):
            for j in range(i+1, len(record)):
                total1 += menu[record[i]][record[j]]

        total2 = 0
        for i in range(len(remain) - 1):
            for j in range(i + 1, len(remain)):
                total2 += menu[remain[i]][remain[j]]

        result.append(abs(total1-total2))
    else:
        for i in range(idx+1, N):
            record.append(i)
            cal(menu, record, result, i)
            record.pop()


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]

    menu = []
    for i in range(N-1):
        combi = []
        for j in range(i+1, N):
            combi.append(food[i][j] + food[j][i])
        menu.append([0] * (i+1) + combi)

    result = []
    cal(menu, [0], result, 0)
    print('#{} {}'.format(tc, min(result)))

