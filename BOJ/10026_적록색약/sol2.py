import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 일반인을 위한 그래프를 만드는 함수
def makeNormalGraph():
    graph = [[] for _ in range(N*N)]

    idx = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N and grid[i][j] == grid[row][col]:
                    graph[idx].append(idx + N*dr[k] + dc[k])
            idx += 1

    return graph


# 적록색약을 위한 그래프를 만드는 함수
def makeBlindGraph():
    graph = [[] for _ in range(N*N)]

    idx = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < N and 0 <= col < N:
                    if grid[i][j] == 'R' or grid[i][j] == 'G':
                        if grid[row][col] == 'R' or grid[row][col] == 'G':
                            graph[idx].append(idx + N*dr[k] + dc[k])
                    else:
                        if grid[i][j] == grid[row][col]:
                            graph[idx].append(idx + N*dr[k] + dc[k])
            idx += 1

    return graph


# dfs 함수. 스택으로 구현!
def dfs(idx, graph, visited):
    to_visit = [idx]

    while to_visit:
        current = to_visit.pop()
        if not visited[current]:
            visited[current] = True
            to_visit += graph[current]


# main
N = int(input())
grid = [list(input().rstrip()) for _ in range(N)]

# 방향을 나타내는 리스트 생성
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 일반인을 위한 그래프 생성
# 그래프 생성 후 연결 요소의 수 구하기
n_graph = makeNormalGraph()
n_visited = [False] * (N*N)
n_district = 0
for i in range(N*N):
    if not n_visited[i]:
        dfs(i, n_graph, n_visited)
        n_district += 1
    elif len(n_graph[i]) == 0:
        n_district += 1

# 적록색맹을 위한 그래프 생성
# 그래프 생성 후 연결 요소의 수 구하기
b_graph = makeBlindGraph()
b_visited = [False] * (N*N)
b_district = 0
for i in range(N*N):
    if not b_visited[i]:
        dfs(i, b_graph, b_visited)
        b_district += 1

# 결과 출력
print(n_district, b_district)