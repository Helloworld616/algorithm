# Prim
# 소요시간 403ms

import sys
import math
sys.stdin = open("input.txt")
# sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')


# 그래프 생성 함수 : 인접 행렬을 만든다!
def make_graph():
    # 그래프 초기화
    graph = [[INF for _ in range(N)] for _ in range(N)]

    # 두 좌표 간의 거리를 그래프에 저장
    for i in range(N):
        for j in range(N):
            graph[i][j] = math.sqrt(pow(location[i][0] - location[j][0], 2) + pow(location[i][1] - location[j][1], 2))

    # 완성된 그래프 반환
    return graph


# 거리값이 최소인 노드를 구하는 함수 : 우선순위 큐의 역할을 대신 함!
def get_min_node():
    # 노드를 0으로 초기화
    node = 0

    # 방문하지 않은 노드를 찾아서 저장! 이걸 비교할 기준값으로 삼는다!
    # 이 과정을 거치지 않으면 계속 0번 노드만 정답으로 나오게 된다.
    for i in range(N):
        if not visited[i]:
            node = i
            break

    # 최소 노드 찾기
    # 아직 방문을 하지 않았고, 현재 노드의 거리보다 더 적은 거리를 가지는 노드가 있다면
    # 노드를 갱신
    for i in range(N):
        if not visited[i] and distances[i] < distances[node]:
            node = i

    # 최소 노드 반환
    return node


# Prim Algorithm
# 첫 번째로 선택한 노드로부터 MST를 만들어 나가는 함수
def prim(first):
    # 첫 번째 노드의 거리를 0으로 저장
    # 자기 자신이라 거리가 없기 떄문!
    distances[first] = 0

    # 노드의 갯수만큼 '출발-도착' 거리를 잰다
    # 현재 거리값 보다 더 최소인 값이 나오면 그 값으로 갱신한다.
    for _ in range(N):
        # 거리값이 최소인 노드를 출발점으로 정하고
        # 출발점 방문 체크
        start = get_min_node()
        visited[start] = True

        # 출발지를 구했으니 이제 모든 도착지와 비교 실시!
        for goal in range(N):
            # 출발지와 연결된 도착지일 경우만 비교 가능
            if adj_matrix[start][goal] != INF:
                # 아직 방문하지 않은 도착지의 거리값이
                # 현재 출발지 - 도착지의 거리보다 클 경우
                # 거리값 갱신
                if not visited[goal] and adj_matrix[start][goal] < distances[goal]:
                    distances[goal] = adj_matrix[start][goal]


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

    adj_matrix = make_graph()  # 인접 행렬 생성
    distances = [INF] * N  # 거리를 기록할 리스트 생성
    visited = [False] * N  # 방문 체크 리스트 생성

    prim(0)  # Prim Algorithm 실행
    payment = cal()  # 환경 부담금 계산

    # 환경 부담금을 반올림한 결과를 출력
    print("#{} {}".format(tc, round(payment)))
