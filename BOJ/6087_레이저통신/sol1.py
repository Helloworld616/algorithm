# 메모리 초과

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# bfs 함수
# C에서 C로 가는 모든 경로들을 저장해서 반환
def bfs(graph):
    queue = deque()
    queue.append([start, [start]])
    visit = [False] * (W*H)
    path = []

    while queue:
        spot = queue.popleft()
        visit[spot[0]] = True
        for i in range(len(graph[spot[0]])):
            dest = graph[spot[0]][i]
            if dest == goal:
                path.append(spot[1]+[dest])
            elif not visit[dest]:
                queue.append([dest, spot[1]+[dest]])

    return path


# main
# 입력 받아 이차원 리스트 생성
W, H = map(int, input().split())
area = [list(input().rstrip()) for _ in range(H)]

# 상하좌우 방향을 저장한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 인접리스트 생성
graph = [[] for _ in range(W*H)]
first = True
idx = 0
for i in range(H):
    for j in range(W):
        if area[i][j] == '.' or area[i][j] == 'C':
            # 시작점과 도착점 저장
            if area[i][j] == 'C' and first:
                start = idx
                first = False
            elif area[i][j] == 'C' and not first:
                goal = idx
            # 상하좌우 탐색을 통해 유망한 정점들 연결
            for k in range(4):
                row = i + dr[k]
                col = j + dc[k]
                if 0 <= row < H and 0 <= col < W:
                    if area[row][col] == '.' or area[row][col] == 'C':
                        graph[idx].append(idx + W*dr[k] + dc[k])
        idx += 1

# bfs를 이용해 C에서 C로 가는 모든 경로들을 찾아서 반환
path = bfs(graph)
# 정답 후보들을 저장할 리스트 candidate 생성
candidate = []

# path 안의 경로들을 모두 비교해서 설치하는 거울의 갯수가 최소가 되는 경우를 구함.
for i in range(len(path)):
    mirror = 0
    if len(path[i]) > 1:
        delta = abs(path[i][1] - path[i][0])
        for j in range(1, len(path[i])):
            if abs(path[i][j] - path[i][j-1]) != delta:
                    mirror += 1
                    delta = abs(path[i][j] - path[i][j-1])
    candidate.append(mirror)

# 정답 후보들 중 최소값을 출력
print(min(candidate))

