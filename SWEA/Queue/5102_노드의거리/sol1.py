import sys
sys.stdin = open('sample_input.txt')
from collections import deque


def bfs(graph, visit, S, G):
    queue = deque()
    queue.append((S, 0))

    while queue:
        node = queue.popleft()
        if node[0] == G:
            return node[1]
        visit[node[0]] = True
        for idx in graph[node[0]]:
            if not visit[idx]:
                queue.append((idx, node[1]+1))

    return 0


T = int(input())


for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visit = [False] * (V + 1)

    for _ in range(E):
        idx1, idx2 = map(int, input().split())
        graph[idx1].append(idx2)
        graph[idx2].append(idx1)

    S, G = map(int, input().split())

    print('#{} {}'.format(tc, bfs(graph, visit, S, G)))