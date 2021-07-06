# Kruskal
# find_parents 함수를 반복문으로 변경

import sys
import math
sys.stdin = open("input.txt")
# sys.stdin = open("sample_input.txt")


INF = float('inf')


def make_sorted_edges():
    edges = []

    for i in range(N-1):
        for j in range(i+1, N):
            edges.append((math.sqrt(pow(location[i][0] - location[j][0], 2) + pow(location[i][1] - location[j][1], 2)), i, j))

    sorted_edges = sorted(edges)
    return sorted_edges


def find_parent(node):
    while parent[node] != node:
        node = parent[node]

    return parent[node]


def make_union(parent1, parent2):
    if rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    elif rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    else:
        parent[parent2] = parent1
        rank[parent1] += 1


def kruskal():
    distances = []

    for edge in sorted_edges:
        distance,  start, goal = edge
        start_parent = find_parent(start)
        goal_parent = find_parent(goal)

        if start_parent != goal_parent:
            make_union(start_parent, goal_parent)
            distances.append(distance)

    return distances


def cal():
    total = 0
    for distance in distances:
        total += pow(distance, 2) * E
    return total


# main
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    location = []
    for i in range(N):
        location.append((X[i], Y[i]))

    sorted_edges = make_sorted_edges()
    visited = [False] * N
    parent = [i for i in range(N)]
    rank = [0] * N

    distances = kruskal()
    payment = cal()

    print("#{} {}".format(tc, round(payment)))
