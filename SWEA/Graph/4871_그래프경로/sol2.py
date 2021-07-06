import sys
sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for i in range(V + 1)]

    for i in range(E):
        start, finish = map(int, input().split())
        graph[start].append(finish)
    S, G = map(int, input().split())

    visit = [0] * (V + 1)
    stack = []
    result = 0
    arrive = S
    stack.append(arrive)

    while stack:
        if arrive == G:
            result = 1
            break
        visit[arrive] = 1
        for vertex in graph[arrive]:
            if not visit[vertex]:
                arrive = vertex
                stack.append(arrive)
                break
        else:
            arrive = stack.pop()

    print('#{} {}'.format(tc, result))


