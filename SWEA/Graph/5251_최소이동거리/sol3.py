import sys
sys.stdin = open("sample_input.txt")


INF = float('inf')


def get_min_node():
    node = 0
    min_value = INF

    for i in range(N+1):
        if not visited[i] and distance[i] < min_value:
            node = i
            min_value = distance[i]

    return node


def dijkstra(first):
    distance[first] = 0

    for _ in range(N):
        start = get_min_node()
        visited[start] = True

        for goal, weight in graph[start]:
            distance[goal] = min(distance[goal], distance[start] + weight)


# main
T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    distance = [INF] * (N+1)
    visited = [False] * (N+1)
    dijkstra(0)

    print("#{} {}".format(tc, distance[N]))

