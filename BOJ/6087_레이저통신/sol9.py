import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 거울 초기화 함수
# 거울을 0개 설치할 수 있는 구역들의 값을 모두 0으로 채워준다.
def initial(mirror):
    queue = deque()

    for i in range(4):
        mirror[start[0]][start[1]][i] = 0
        # 큐에 위치, 방향 저장
        queue.append([start, i])

    # 시작 위치로부터 상하좌우에 위치한 구역들을 모두 0으로 초기화
    # 초기화한 후 해당 구역들을 큐에 저장
    # BFS는 초기화한 구역들로부터 시작되어야 하기 때문
    row = start[0]
    col = start[1]
    for i in range(4):
        n_row = row + dr[i]
        n_col = col + dc[i]
        while 0 <= n_row < H and 0 <= n_col < W and area[n_row][n_col] != '*':
            queue.append([(n_row, n_col), i])
            mirror[n_row][n_col][i] = 0
            n_row += dr[i]
            n_col += dc[i]

    return queue


# 설치해야할 거울의 최솟값을 반환하는 함수
def install(mirror):
    # 함수 initial로부터 큐를 받아온다.
    queue = initial(mirror)
    # 만들어야 할 거울의 수는 1부터 시작한다.
    # 0개를 설치할 수 있는 공간들을 이미 다 채워주었기 때문!
    make = 1

    # 탐색 시작
    # BFS와 DFS를 혼합한 듯한 탐색이다.
    # 큐로부터 시작 위치들을 가져온 뒤, 시작 위치들로부터 상하좌우에 있는 곳들을 모두 make로 채워준다.
    while queue:
        # 큐의 길이를 미리 저장
        # BFS 탐색 이전에 상하좌우 탐색을 먼저 해야하기 때문이다!
        # 큐의 길이 저장 -> 큐의 길이 만큼 상하좌우 탐색 -> 탐색한 장소에 make 집어넣기 -> 큐로 저장 후 bfs 탐색
        length = len(queue)
        for _ in range(length):
            # 출발 위치 꺼내기
            now = queue.popleft()
            row = now[0][0]
            col = now[0][1]
            move = now[1]
            # 상하좌우 탐색 시작!
            # 다만 이미 지나온 방향은 제외한다.
            for i in range(4):
                if move != i:
                    # 상하좌우 탐색을 가능한 한 시행하여 탐색 장소에 make를 집어넣는다.
                    # 탐색한 장소는 BFS를 위해 큐에 집어넣는다.
                    n_row = row + dr[i]
                    n_col = col + dc[i]
                    while 0 <= n_row < H and 0 <= n_col < W and area[n_row][n_col] != '*'and mirror[n_row][n_col][move] == 10000:
                        queue.append([(n_row, n_col), i])
                        mirror[n_row][n_col][now[1]] = make
                        n_row += dr[i]
                        n_col += dc[i]
        # 가능한 상하좌우 탐색이 다 끝나면 make를 1 증가시킨다.
        make += 1

    return min(mirror[goal[0]][goal[1]])


# main
# 입력 받아 이차원 리스트 생성
W, H = map(int, input().split())
area = [list(input().rstrip()) for _ in range(H)]
mirror = [[[10000]*4 for _ in range(W)] for _ in range(H)]
first = True

# 시작점과 도착점 찾아서 저장
for i in range(H):
    for j in range(W):
        if area[i][j] == 'C' and first:
            start = (i, j)
            first = False
        elif area[i][j] == 'C' and not first:
            goal = (i, j)

# 상하좌우 방향을 저장한 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 설치해야 할 거울의 최소값 출력
print(install(mirror))