import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    num, N = map(int, input().split())
    road = list(map(int, input().split()))
    field = [[] for _ in range(100)]

    for i in range(0, len(road), 2):
        field[road[i]].append(road[i+1])

    visit = [0] * 100
    result = 0
    arrive = 0
    stack = [arrive]

    while stack:
        if arrive == 99:
            result = 1
            break
        visit[arrive] = 1
        for vertex in field[arrive]:
            if not visit[vertex]:
                arrive = vertex
                stack.append(arrive)
                break
        else:
            arrive = stack.pop()

    print('#{} {}'.format(tc, result))

