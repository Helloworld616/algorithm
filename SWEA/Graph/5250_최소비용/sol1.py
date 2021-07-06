# 시간초과

import sys
sys.stdin = open("sample_input.txt")

INF = float('inf')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def make_graph():
    graph = [[] for _ in range(destination)]

    idx = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N:
                    cost = 1
                    if matrix[row][col] > matrix[i][j]:
                        cost += matrix[row][col] - matrix[i][j]
                    graph[idx].append((idx + dr[k] * N + dc[k], cost))
            idx += 1

    return graph


def get_min_node():
    node = 0
    for i in range(destination):
        if not visited[i]:
            node = i
            break

    for i in range(destination):
        if not visited[i] and distances[i] < distances[node]:
            node = i

    return node


def dijkstra(first):
    distances[first] = 0
    visited[first] = True

    for info in adj_list[first]:
        distances[info[0]] = info[1]

    for i in range(destination-1):
        start = get_min_node()
        visited[start] = True
        for goal, cost in adj_list[start]:
            distances[goal] = min(distances[goal], distances[start] + cost)


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    destination = N * N

    adj_list = make_graph()
    visited = [False] * destination
    distances = [INF] * destination
    dijkstra(0)

    print("#{} {}".format(tc, distances[destination-1]))

