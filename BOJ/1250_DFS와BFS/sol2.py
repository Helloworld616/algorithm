import sys
from collections import deque


# dfs
# 재귀를 통해 깊게 들어감. visit를 통해 방문 여부 체크.
def dfs(graph, arrive, result1, visit):
    visit[arrive] = 1
    result1.append(arrive)
    for vertex in graph[arrive]:
        if not visit[vertex]:
            dfs(graph, vertex, result1, visit)


# bfs
# 큐와 반복문을 통해 같은 너비의 vertex를 먼저 탐색. visit를 통해 방문 여부 체크.
def bfs(graph, result2, N, V):
    queue = deque()
    visit = [0] * (N + 1)

    queue.append(V)
    result2.append(V)
    visit[V] = 1

    while queue:
        arrive = queue.popleft()
        for vertex in graph[arrive]:
            if not visit[vertex]:
                queue.append(vertex)
                result2.append(vertex)
                visit[vertex] = 1


# main
# 입력 받아 그래프 생성
N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    vertex1, vertex2 = map(int, sys.stdin.readline().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

# 결과를 저장할 리스트와 방문을 기록할 리스트 생
result1 = []
result2 = []
visit = [0] * (N + 1)

# 그래프를 정렬
for i in range(len(graph)):
    graph[i] = sorted(graph[i])

# dfs 실행 및 출력
visit[V] = 1
result1.append(V)
for arrive in graph[V]:
    if not visit[arrive]:
        dfs(graph, arrive, result1, visit)
print(' '.join(map(str, result1)))

# bfs 실행 및 출력
bfs(graph, result2, N, V)
print(' '.join(map(str, result2)))
