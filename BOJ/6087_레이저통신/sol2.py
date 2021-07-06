# 실패

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# bfs 함수
def bfs(graph):
    # 큐 생성 후 첫 번째 원소 추가
    queue = deque()
    queue.append([start])

    # 맨 처음과 이후를 나눌 변수 first
    first = True
    # 첫 경로를 찾았을 때와 그렇지 않았을 때를 나눌 변수 flag
    flag = False

    # 방문 여부를 체크할 리스트 visit 생성
    # 출발지에 방문 표시
    visit = [False] * (W*H)
    visit[start] = True

    # 거울 갯수
    mirror = 0

    # bfs 실행
    while queue:
        # 큐의 맨 앞의 원소 추출
        spot = queue.popleft()

        # 첫 탐색일 경우
        if first:
            # first를 False로 변경
            first = False
            # 인접 리스트 탐색
            for i in range(len(graph[spot[0]])):
                dest = graph[spot[0]][i]
                # 목적지를 발견했을 경우 바로 결과 반환
                if dest == goal:
                    return mirror
                # 아닐 경우 방문 체크하고 큐에 추가
                elif not visit[dest]:
                    visit[dest] = True
                    # 큐에 추가하는 리스트 : [다음 장소, 다음 장소와 현 위치 간의 거리, 거울 갯수]
                    queue.append([dest, dest - spot[0], 0])

        # 첫 탐색이 아닐 경우
        else:
            # 인접 리스트 탐색
            for i in range(len(graph[spot[0]])):
                dest = graph[spot[0]][i]

                # 첫 경로를 발견했을 경우
                if flag:
                    # 목적지를 발견했을 경우 기존의 mirror 값과 현재 거울 개수를 비교하여 더 작은 값으로 mirror를 갱신
                    if dest == goal:
                        if abs(dest - spot[0]) != spot[1]:
                            if spot[2]+1 < mirror:
                                mirror = spot[2]+1
                        else:
                            if spot[2] < mirror:
                                mirror = spot[2]
                    # 목적지를 발견하지 못했을 경우
                    # 방문을 하지 않았고 현재 거울 개수가 mirror 보다 작은 경우에만 다음 장소로 이동
                    elif not visit[dest] and spot[2] < mirror:
                        visit[dest] = True
                        # 다음 장소의 거리가 기존의 거리와 다를 경우 거울 갯수 1 증가
                        if abs(dest - spot[0]) != spot[1]:
                            queue.append([dest, abs(dest - spot[0]), spot[2]+1])
                        # 다음 장소의 거리가 기존의 거리와 같을 경우 거울 갯수는 그대로
                        else:
                            queue.append([dest, abs(dest - spot[0]), spot[2]])
                # 첫 경로를 발견하지 못했을 경우
                else:
                    # 목적지를 발견했을 경우 flag를 True로 바꾸고 mirror의 값 갱신
                    if dest == goal:
                        flag = True
                        if abs(dest - spot[0]) != spot[1]:
                            mirror = spot[2]+1
                        else:
                            mirror = spot[2]
                    # 목적지를 발견하지 못했을 경우
                    # 방문하지 않았을 경우만 탐색
                    elif not visit[dest]:
                        # 방문 표시
                        visit[dest] = True
                        # 다음 장소의 거리가 기존의 거리와 다를 경우 거울 갯수 1 증가
                        # print(dest, spot[0], spot[1], spot[2])
                        if abs(dest - spot[0]) != spot[1]:
                            queue.append([dest, abs(dest - spot[0]), spot[2]+1])
                        # 다음 장소의 거리가 기존의 거리와 같을 경우 거울 갯수는 그대로
                        else:
                            queue.append([dest, abs(dest - spot[0]), spot[2]])

    return mirror


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

print(bfs(graph))