# Bellman-Ford

import sys
sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


def bellman_ford(start):
    distance = [INF] * (N + 1)  # 뱡문 체크 리스트 생성 및 초기화
    distance[start] = 0  # 첫 번째 노드의 거리 비용을 0으로 저장

    # 각 노드로 갈 수 있는 최소 이동 거리를 구한다.
    for _ in range(N):  # 노드 사이의 거리 갯수만큼만 구하면 되므로 (노드 - 1)만큼만 실행!
        for start in range(N+1):  # 노드에서 출발점을 하나씩 꺼낸다.
            for goal, weight in graph[start]:  # 출발점에서 갈 수 있는 목적지와, 목적지까지의 비용을 꺼낸다.
                # 이 부분은 다익스트라와 아이디어가 똑같다!
                # (출발지의 거리 비용 + 출발지에서 목적지로 가는 비용)과 (목적지의 거리 비용) 중 더 작은 것을 선택한다.
                # 이 과정을 거쳐 distance에는 최소값만 저장이 됨!
                distance[goal] = min(distance[goal], distance[start] + weight)

    # Bellman-Ford의 특징 : 음수 싸이클 존재 여부 점검
    for start in range(N + 1):
        for goal, weight in graph[start]:
            # 만약 목적지의 거리 비용이 아직도 최소화될 여지가 남아 있다면
            # 그것은 음수 싸이클이 존재한다는 의미이다!
            if distance[goal] > distance[start] + weight:
                return []  # 음수 싸이클이 존재할 경우 정상적인 최단경로를 구할 수 없으므로 빈 리스트 반환

    # 음수 싸이클이 존재하지 않을 경우, 산출된 distance 반환
    return distance


# main
T = int(input())

for tc in range(1, T + 1):
    # 마지막 연결 지점 번호와 도로의 개수 입력 받기
    N, E = map(int, input().split())

    # 그래프 생성
    graph = [[] for _ in range(N + 1)]
    # 간선 정보를 입력 받아 그래프에 추가한다.
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    # Bellman-Ford 알고리즘으로 구한 거리 리스트를 받는다.
    ans = bellman_ford(0)

    # 빈 리스트가 아닐 경우 N번째 값 출력
    if len(ans):
        print("#{} {}".format(tc, ans[N]))
