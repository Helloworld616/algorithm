# Kruskal
# 소요시간 3021ms

import sys
import math
sys.stdin = open("input.txt")
# sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


# 거리를 기준으로 정렬된 간선 리스트를 생성하는 함수
def make_sorted_edges():
    # 리스트 생성 및 초기화
    edges = []

    # 두 노드와 노드 간의 거리를 리스트에 담는다.
    for i in range(N-1):
        for j in range(i+1, N):
            edges.append((i, j, math.sqrt(pow(location[i][0] - location[j][0], 2) + pow(location[i][1] - location[j][1], 2))))

    # 리스트를 거리를 기준으로 정렬한다.
    sorted_edges = sorted(edges, key=lambda x: x[2])

    # 정렬된 리스트 반환
    return sorted_edges


# 최상위 부모(조상)를 찾는 함수
# Path Compression 기법 적용
def find_parent(node):
    # 부모가 자기 자신이 아니면
    # 현재의 부모 노드로 바로 이동
    if parent[node] != node:
        parent[node] = find_parent(parent[node])

    # 부모가 자기 자신일 때 부모 값 반환
    return parent[node]


# union 연산 알고리즘
def union(parent1, parent2):
    # 조상을 비교해서 랭크가 큰 것을, 랭크가 작은 것의 부모로 설정
    if rank[parent1] > rank[parent2]:
        parent[parent2] = parent1
    elif rank[parent1] < rank[parent2]:
        parent[parent1] = parent2
    # 조상의 랭크가 같을 경우
    # 한 쪽의 부모를 다른 한 쪽으로 갱신해준 다음
    # 부모가 된 노드의 랭크를 1 증가시킴
    else:
        parent[parent2] = parent1
        rank[parent1] += 1


# Kruskal Algorithm
def kruskal():
    # 거리를 저장할 리스트 생성 및 초기화
    distances = []

    # 정렬된 간선 리스트에서 간선을 하나 꺼낸다.
    for edge in sorted_edges:
        # 간선의 출발지, 도착지, 거리 정보를 변수에 담는다.
        start, goal, distance = edge
        # 출발지의 조상과 도착지의 조상을 각각 구한다.
        start_parent = find_parent(start)
        goal_parent = find_parent(goal)

        # 두 노드의 조상이 다를 경우는 싸이클이 아니므로
        # union 연산 실시 및 거리 추가
        if start_parent != goal_parent:
            union(start_parent, goal_parent)
            distances.append(distance)

    # 최종적으로 산출된 거리 리스트 반환
    return distances


# 환경 부담금 계산 함수
def cal():
    # 총 부담금 초기화
    total = 0
    # 거리를 하나씩 꺼내서 계산
    for distance in distances:
        total += pow(distance, 2) * E
    # 계산 결과 반환
    return total


# main
T = int(input())

for tc in range(1, T+1):
    # 섬의 크기, X좌표, Y좌표, 세율 입력 받기
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 분리된 X, Y 좌표를 한 쌍씩 묶어서 리스트로 관리
    location = []
    for i in range(N):
        location.append((X[i], Y[i]))

    sorted_edges = make_sorted_edges()  # 간선을 거리를 기준으로 정렬한 리스트 생성
    visited = [False] * N  # 방문 체크 리스트 생성
    parent = [i for i in range(N)]  # 부모 정보를 담는 리스트 생성. 처음 부모는 자기 자신으로 초기화.
    rank = [0] * N  # 랭크 정보를 담는 리스트 생성. 랭크는 0으로 초기화.

    distances = kruskal()  # Kruskal Algorithm 실행
    payment = cal()  # 환경 부담금 계산

    # 환경 부담금을 반올림한 결과를 출력
    print("#{} {}".format(tc, round(payment)))
