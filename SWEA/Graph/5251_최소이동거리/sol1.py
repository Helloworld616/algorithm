# Dijkstra

import sys
sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


# 거리 비용이 최소인 노드를 구하는 함수 : 우선순위 큐의 역할을 대신 함!
def get_min_node():
    # 노드와 최소 비용을 초기화
    node = 0
    min_weight = INF

    # 노드 탐색
    for i in range(N+1):
        # 아직 방문을 하지 않은 노드의 거리 비용이 최소 비용보다 작을 경우
        # 노드와 최소 비용을 갱신
        if not visited[i] and distance[i] < min_weight:
            node = i
            min_weight = distance[i]

    # 최종적으로 산출된 최소 노드 반환
    return node


# 다익스트라 알고리즘 구현 함수
def dijkstra(first):
    # 첫 번째 노드의 거리 가중치를 0으로 저장
    distance[first] = 0

    # 각 노드로 갈 수 있는 최소 이동 거리를 구한다.
    # 노드 사이의 거리 갯수만큼만 구하면 되므로 (노드 - 1)만큼만 실행!
    for _ in range(N):
        # 가중치가 최소인 노드를 출발지로 정하고
        # 출발지 방문 체크
        start = get_min_node()
        visited[start] = True

        # 출발지를 구했으니 이제는 목적지를 체크한다!
        # (출발지의 거리 비용 + 출발지에서 목적지로 가는 비용)과
        # (목적지의 거리 비용) 중 더 작은 것을 선택한다.
        # 이 과정을 거쳐 distance에는 최소값만 저장이 됨!
        for goal, weight in graph[start]:
            distance[goal] = min(distance[goal], distance[start] + weight)


# main
T = int(input())

for tc in range(1, T+1):
    # 마지막 연결 지점 번호와 도로의 개수 입력 받기
    N, E = map(int, input().split())

    # 그래프 생성
    graph = [[] for _ in range(N + 1)]
    # 간선 정보를 입력 받아 그래프에 추가한다.
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # 거리 리스트, 뱡문 체크 리스트 생성 및 초기화
    distance = [INF] * (N + 1)
    visited = [False] * (N + 1)

    # 다익스트라 알고리즘 실행
    dijkstra(0)

    # 목적지까지의 최소이동거리 출력
    print("#{} {}".format(tc, distance[N]))
