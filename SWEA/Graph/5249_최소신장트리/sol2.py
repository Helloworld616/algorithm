import sys
sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


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
def do_union(parent1, parent2):
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
    # 최소 신장 트리의 거리를 0으로 초기화
    mst_distance = 0

    # 간선 리스트에서 간선을 하나 꺼낸다.
    for edge in edges:
        # 간선의 출발지, 도착지, 거리 정보를 변수에 담는다
        start, goal, distance = edge
        # 출발지의 조상과 도착지의 조상을 각각 구한다.
        s_parent = find_parent(start)
        g_parent = find_parent(goal)

        # 두 노드의 조상이 다를 경우는 싸이클이 아니므로
        # union 연산 실시 및 거리 추가
        if s_parent != g_parent:
            do_union(s_parent, g_parent)
            mst_distance += distance

    # 최종적으로 산출된 최소 신장 트리의 거리를 반환
    return mst_distance


# main
T = int(input())

for tc in range(1, T+1):
    # 노드 번호와 간선 입력 받기
    V, E = map(int, input().split())

    # 간선 정보 입력 받기
    # 입력을 받은 후, 가중치를 기준으로 정렬
    edges = []
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    edges.sort(key=lambda x: x[2])

    # 거리 리스트, 뱡문 체크 리스트, 부모 리스트, 랭크 리스트 생성 및 초기화
    distances = [INF] * (V+1)
    visited = [False] * (V+1)
    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    # 산출한 최소 신장 트리의 거리 총합 출력
    print("#{} {}".format(tc, kruskal()))
