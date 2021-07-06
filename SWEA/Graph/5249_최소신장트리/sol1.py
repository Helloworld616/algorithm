# Prim

import sys
sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


# 가중치가 최소인 노드를 구하는 함수 : 우선순위 큐의 역할을 대신 함!
def get_min_node():
    # 노드를 0으로 초기화
    node = 0

    # 방문하지 않은 노드를 찾아서 저장! 이걸 비교할 기준값으로 삼는다!
    # 이 과정을 거치지 않으면 계속 0번 노드만 정답으로 나오게 된다.
    for i in range(V+1):
        if not visited[i]:
            node = i
            break

    # 최소 노드 찾기
    # 아직 방문을 하지 않았고, 현재 노드의 가중치보다 더 적은 가중치를 가지는 노드가 있다면
    # 노드를 갱신
    for i in range(V+1):
        if not visited[i] and distances[i] < distances[node]:
            node = i

    # 최소 노드 반환
    return node


# Prim Algorithm
# 첫 번째로 선택한 노드로부터 MST를 만들어 나가는 함수
def prim(first):
    # 첫 번째 노드의 거리 가중치를 0으로 저장
    # 자기 자신이라 거리가 없기 떄문!
    distances[first] = 0

    # 노드의 갯수만큼 '출발-도착' 사이의 가중치를 잰다
    # 현재 거리값 보다 더 최소인 가중치가 나오면 그 값으로 갱신한다.
    for _ in range(V+1):
        # 가중치가 최소인 노드를 출발점으로 정하고
        # 출발점 방문 체크
        start = get_min_node()
        visited[start] = True

        # 출발지를 구했으니 이제 모든 도착지와 비교 실시!
        for goal, weight in graph[start]:
            # 아직 방문하지 않은 도착지의 가중치가
            # 현재 출발지-도착지 사이의 가중치보다 클 경우 갱신
            if not visited[goal] and weight < distances[goal]:
                distances[goal] = weight


# main
T = int(input())

for tc in range(1, T+1):
    # 노드 번호와 간선 입력 받기
    V, E = map(int, input().split())
    # 그래프 생성 및 초기화
    graph = [[] for _ in range(V+1)]

    # 그래프(인접 리스트) 생성
    # 양 방향 그래프이므로 출발지, 도착지 모두에 간선 정보를 추가
    for _ in range(E):
        s, g, w = map(int, input().split())
        graph[s].append((g, w))
        graph[g].append((s, w))

    # 거리 리스트, 뱡문 체크 리스트 생성 및 초기화
    distances = [INF] * (V+1)
    visited = [False] * (V+1)

    # 프림 알고리즘 실행
    prim(0)

    # 산출한 최소 신장 트리의 거리 가중치 총합 출력
    print("#{} {}".format(tc, sum(distances)))
