import sys
sys.stdin = open("sample_input.txt")

INF = float('inf')


def get_min_node():
    node = 0
    min_value = INF

    for i in range(len(distance)):
        if not visited[i] and distance[i] < min_value:
            node = i
            min_value = distance[i]

    return node


def prim(first):
    distance[first] = 0

    for _ in range(V+1):
        start = get_min_node()
        visited[start] = True

        for goal, weight in graph[start]:
            if not visited[goal] and distance[goal] > weight:
                distance[goal] = weight


# main
T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        s, g, w = map(int, input().split())
        graph[s].append((g, w))
        graph[g].append((s, w))

    distance = [INF] * (V + 1)
    visited = [False] * (V + 1)
    prim(0)

    print("#{} {}".format(tc, sum(distance)))

