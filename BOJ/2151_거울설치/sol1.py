import sys
from collections import deque
sys.stdin = open('input.txt')


# bfs 탐색 함수
def bfs(ud_graph, lr_graph, start, end, vertical):
    # 큐 생성 및 변수 초기화
    queue = deque()
    answer = 2501
    flag = False

    # vertical 값이 True일 경우 '상하 -> 좌우' 탐색 실시
    if vertical:
        queue.append((ud_graph[start], 1))
        while queue:
            location = queue.popleft()
            # 문의 위치에 도달했을 경우 반복문을 빠져나오고 횟수를 출력
            # 문의 위치에 도달하지 않았을 경우 현재 방향으로부터 수직 방향 탐색을 실시
            for idx in location[0]:
                if idx == end:
                    flag = True
                    answer = location[1] - 1
                    break
                else:
                    if location[1] % 2:
                        queue.append((lr_graph[idx], location[1] + 1))
                    else:
                        queue.append((ud_graph[idx], location[1] + 1))
            if flag:
                break
    # vertical 값이 False일 경우 '좌우 -> 상하' 탐색 실시
    else:
        queue.append((lr_graph[start], 1))
        while queue:
            location = queue.popleft()
            # 문의 위치에 도달했을 경우 반복문을 빠져나오고 횟수를 출력
            # 문의 위치에 도달하지 않았을 경우 현재 방향으로부터 수직 방향 탐색을 실시
            for idx in location[0]:
                if idx == end:
                    flag = True
                    answer = location[1] - 1
                    break
                else:
                    if location[1] % 2:
                        queue.append((ud_graph[idx], location[1] + 1))
                    else:
                        queue.append((lr_graph[idx], location[1] + 1))
            if flag:
                break

    return answer


# main
# 입력 받아 리스트 생성하기
N = int(sys.stdin.readline())
room = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# 이동방향 담은 리스트 move
move = [1, -1]

# 상하연결 그래프, 좌우연결 그래프 생성
ud_graph = [[] for _ in range(N**2)]
lr_graph = [[] for _ in range(N**2)]
# 그래프 인덱스 초기화
idx = 0
first = True

# 리스트를 순회하면서 상하/좌우 인접 요소들 확인
for i in range(N):
    for j in range(N):
        # 리스트의 값이 '문'이거나 '거울 설치 장소'일 때만 요소 연결
        if room[i][j] == '#' or room[i][j] == '!':
            # 리스트의 값이 문일 경우 위치 저장
            # 두 개의 문의 위치는 bfs 탐색을 할 때 각각 시작점과 끝점이 된다.
            if room[i][j] == '#':
                if first:
                    start = idx
                    first = False
                else:
                    end = idx
            # 상하/좌우로 이동하면서 행/열의 요소들 확인
            for m in move:
                # 상하로 이동하면서 열의 요소들 확인
                # 요소가 문이거나 거울 설치 장소일 경우 연결
                # 벽일 경우 탐색 중지
                n = 1
                while 0 <= i + n * m < N:
                    if room[i + n * m][j] == '!' or room[i + n * m][j] == '#':
                        ud_graph[idx].append(idx + n * N * m)
                    elif room[i + n * m][j] == '*':
                        break
                    n += 1
                # 좌우로 이동하면서 열의 요소들 확인
                # 요소가 문이거나 거울 설치 장소일 경우 연결
                # 벽일 경우 탐색 중지
                n = 1
                while 0 <= j + n * m < N:
                    if room[i][j + n * m] == '!' or room[i][j + n * m] == '#':
                        lr_graph[idx].append(idx + n * m)
                    elif room[i][j + n * m] == '*':
                        break
                    n += 1
        # 그래프 인덱스 1 증가
        idx += 1

# bfs 탐색은 두 번 이루어져야 한다.
# '상하 -> 좌우' 탐색과 '좌우 -> 상하' 탐색
# 탐색해서 나온 값들 중 더 작은 값을 출력
print(min(bfs(ud_graph, lr_graph, start, end, True), bfs(ud_graph, lr_graph, start, end, False)))

