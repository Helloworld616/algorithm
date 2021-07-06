# 시간초과

import sys
sys.stdin = open("input.txt")


INF = float('inf')


def find_distance(start, goal):
    distances = []

    for r1, c1 in start:
        distance = []
        for r2, c2 in goal:
            distance.append(abs(r1-r2) + abs(c1-c2))
        distances.append(distance)

    return distances


def make_compare():
    min_distances = [INF] * H

    for i in range(len(h_to_c)):
        for j in range(C):
            if not visited[j]:
                if h_to_c[i][j] < min_distances[i]:
                    min_distances[i] = h_to_c[i][j]

    return sum(min_distances)


def find_min_distance(choose):
    global min_distance
    flag = True

    if len(c_to_h) - choose == M:
        # print(len(distances) - choose)
        compare = make_compare()
        if compare < min_distance:
            min_distance = compare
        else:
            flag = False

    if flag:
        for i in range(len(c_to_h)):
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
C = 0
for i in range(N):
    for j in range(N):
        if town[i][j] == 1:
            houses.append((i, j))
            H += 1
        if town[i][j] == 2:
            chickens.append((i, j))
            C += 1

c_to_h = find_distance(chickens, houses)
h_to_c = find_distance(houses, chickens)

visited = [False] * len(c_to_h)
min_distance = INF

find_min_distance(0)
print(min_distance)