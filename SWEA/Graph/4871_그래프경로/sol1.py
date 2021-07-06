import sys
sys.stdin = open('sample_input.txt')


def dfs(graph, idx, visit, result, G):
    visit[idx] = 1
    if idx == G:
        result[0] = 1
    for road in graph[idx]:
        if not visit[road]:
            dfs(graph, road, visit, result, G)


T = int(input())


for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]

    for i in range(E):
        start, finish = map(int, input().split())
        graph[start].append(finish)
    S, G = map(int, input().split())

    visit = [0] * (V+1)
    result = [0]

    for start in graph[S]:
        dfs(graph, start, visit, result, G)

    print('#{} {}'.format(tc, result[0]))
