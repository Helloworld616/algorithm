# 시간초과

import sys
sys.stdin = open("input.txt")


INF = float('inf')


def find_distance():
    distances = []

    for r1, c1 in chickens:
        distance = []
        for r2, c2 in houses:
            distance.append(abs(r1-r2) + abs(c1-c2))
        distances.append(distance)

    return distances


def make_compare():
    candidates = []
    for i in range(len(distances)):
        if not visited[i]:
            candidates.append(distances[i])

    min_distances = [INF] * H
    for i in range(len(candidates)):
        for j in range(H):
            if candidates[i][j] < min_distances[j]:
                min_distances[j] = candidates[i][j]

    return sum(min_distances)


def find_min_distance(choose):
    global min_distance

    if choose == len(distances):
        return

    if len(distances) - choose <= M:
        # print(len(distances) - choose)
        compare = make_compare()
        if compare < min_distance:
            min_distance = compare
    else:
        for i in range(len(distances)):
            if not visited[i]:
                visited[i] = True
                if make_compare() < min_distance:
                    find_min_distance(choose + 1)
                visited[i] = False


# main
N, M = map(int, input().split())
town = [list(map(int, input().split())) for _ in range(N)]

houses = []
chickens = []
H = 0
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            houses.append((i, j))
            H += 1
        if town[i][j] == 2:
            chickens.append((i, j))

distances = find_distance()
# print(distances)
visited = [False] * len(distances)
min_distance = INF

find_min_distance(0)
print(min_distance)

