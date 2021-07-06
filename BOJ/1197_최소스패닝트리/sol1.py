import sys
input = sys.stdin.readline

INF = float('inf')


def get_min_node():
    node = 0

    for i in range(V + 1):
        if not visited[i]:
            node = i
            break

    for i in range(V + 1):
        if not visited[i] and distance[i] < distance[node]:
            node = i

    return node


def prim(first):
    distance[first] = 0

    for _ in range(V + 1):
        start = get_min_node()
        visited[start] = True

        for goal, weight in graph[start]:
            if not visited[goal] and weight < distance[goal]:
                distance[goal] = weight


# main
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]

for tc in range(E):
    s, g, w = map(int, input().split())
    graph[s].append((g, w))
    graph[g].append((s, w))

distance = [INF] * (V + 1)
visited = [False] * (V + 1)

prim(1)

print(sum(distance[1:]))




