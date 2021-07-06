import sys
sys.stdin = open("sample_input.txt")


def find_root(node):
    if parent[node] != node:
        parent[node] = find_root(parent[node])

    return parent[node]


def union(parent1, parent2):
    if rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    elif rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    else:
        rank[parent1] += 1
        parent[parent2] = parent1


def kruskal():
    mst = 0

    for start, goal, weight in edges:
        s_parent = find_root(start)
        g_parent = find_root(goal)

        if s_parent != g_parent:
            union(s_parent, g_parent)
            mst += weight

    return mst


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    edges = []
    for _ in range(E):
        s, g, w = map(int, input().split())
        edges.append((s, g, w))
    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    print("#{} {}".format(tc, kruskal()))
