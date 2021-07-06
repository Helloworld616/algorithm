import sys
sys.stdin = open('input.txt')


def dfs(field, idx, result):
    visit[idx] = 1
    if idx == 99:
        result[0] = 1
    for vertex in field[idx]:
        if not visit[vertex]:
            dfs(field, vertex, result)


for tc in range(1, 11):
    num, N = map(int, input().split())
    road = list(map(int, input().split()))
    field = [[] for _ in range(100)]

    for i in range(0, len(road), 2):
        field[road[i]].append(road[i+1])

    visit = [0] * 100
    result = [0]

    for idx in field[0]:
        dfs(field, idx, result)

    print('#{} {}'.format(tc, result[0]))





