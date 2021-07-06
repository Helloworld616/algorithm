import sys
from collections import deque
sys.stdin = open("sample_input.txt")

# 전역변수 무한대 선언
INF = float('inf')

# 상하좌우 4방향을 나타내는 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 그래프 생성 함수 : 인접 리스트를 생성!
def make_graph():
    graph = [[] for _ in range(destination)]  # 그래프 생성
    idx = 0  # 그래프 인덱스 초기화

    # 배열의 모든 좌표에 대하여
    for i in range(N):
        for j in range(N):
            # 상하좌우 탐색을 실시
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                # 상하좌우 좌표가 배열의 범위 안에 있을 경우
                if 0 <= row < N and 0 <= col < N:
                    # 위치와 비용을 그래프에 추가
                    cost = 1
                    # 좌표의 값이 현재보다 클 경우 추가 비용 계산
                    if matrix[row][col] > matrix[i][j]:
                        cost += matrix[row][col] - matrix[i][j]
                    graph[idx].append((idx + dr[k] * N + dc[k], cost))
            # 인덱스 1 증가
            idx += 1

    # 완성된 그래프 반환
    return graph


# bfs 함수
def bfs():
    # 큐 생성
    queue = deque()

    # 큐에 출발지를 넣고, 출발지의 거리를 0으로 초기화한다.
    queue.append(0)
    distance[0] = 0

    # bfs 시작
    while queue:
        # 큐에서 그래프의 인덱스를 꺼낸다.
        idx = queue.popleft()
        # 해당 인덱스의 인접 노드와 비용을 꺼낸다.
        for vertex, cost in adj_list[idx]:
            # Dijkstra의 아이디어 차용
            # (현재 인덱스의 거리 비용 + 인접 노드로 가는 데에 드는 비용)이
            # 인접 노드의 거리 비용보다 작을 경우 갱신
            # 갱신이 이루어질 경우 큐에 인접 노드를 넣는다.
            if distance[idx] + cost < distance[vertex]:
                distance[vertex] = distance[idx] + cost
                queue.append(vertex)


# main
T = int(input())

for tc in range(1, T+1):
    # 배열의 크기와 배열 입력 받기
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    destination = N * N  # 목적지 설정
    adj_list = make_graph()  # 그래프(인접 리스트) 생성
    distance = [INF] * destination  # 거리 리스트 생성 및 초기화

    # bfs 탐색 실시
    bfs()

    # 목적지까지의 최단 거리 출력
    print("#{} {}".format(tc, distance[destination-1]))
