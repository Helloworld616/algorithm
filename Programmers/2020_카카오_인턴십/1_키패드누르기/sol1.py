import sys
from collections import deque
sys.stdin = open("input.txt")


# bfs 함수
def bfs(start, goal):
    # 상하좌우 4방향을 나타내는 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 방문 배열 초기화
    visited = [[-1 for _ in range(3)] for _ in range(4)]
    visited[start[0]][start[1]] = 0

    # 만약 출발점과 도착점이 같다면 바로 결과값 반환
    if start[0] == goal[0] and start[1] == goal[1]:
        return visited[start[0]][start[1]]

    # BFS 탐색을 위한 큐 생성. 생성 후 출발 좌표 넣기.
    queue = deque()
    queue.append(start)

    # BFS 시작
    while queue:
        # 큐에서 좌표 추출
        spot = queue.popleft()
        row = spot[0]
        col = spot[1]

        # 4방향 탐색
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            # 유효 범위 안에 있고 아직 방문하지 않았을 경우
            if 0 <= n_row < 4 and 0 <= n_col < 3 and visited[n_row][n_col] == -1:
                # 방문 체크한 뒤 거리를 1 늘림!
                visited[n_row][n_col] = visited[row][col] + 1
                # 방문할 곳이 도착점과 같다면 바로 결과값 반환
                if n_row == goal[0] and n_col == goal[1]:
                    return visited[n_row][n_col]
                # 새로운 좌표를 큐에 삽입
                queue.append((n_row, n_col))


# 답안 함수
def solution(numbers, hand):
    answer = ''  # 답안 초기화
    # 각 번호를 입력해야 하는 손가락 정보 저장
    # L은 왼손, R은 오른손, M은 중앙에 있는 번호들
    keyhand = ['M', 'L', 'M', 'R', 'L', 'M', 'R', 'L', 'M', 'R']

    # 각 번호의 좌표 저장
    location = []
    for i in range(3):
        for j in range(3):
            location.append((i, j))
    
    # 0의 좌표도 추가하고
    location.insert(0, (3, 1))
    # 왼손 출발점과 오른손 출발점을 설정한다.
    left = (3, 0)
    right = (3, 2)

    # 주어진 번호 리스트에서 번호를 하나씩 꺼낸다.
    for number in numbers:
        # 왼손으로 쳐야하는 번호일 경우
        # 좌표 옮기고 정답에 L 추가
        if keyhand[number] == 'L':
            left = location[number]
            answer += 'L'
        # 오른손으로 쳐야하는 번호일 경우
        # 좌표 옮기고 정답에 R 추가
        elif keyhand[number] == 'R':
            right = location[number]
            answer += 'R'
        # 가운데에 있는 번호일 경우
        else:
            # 왼손으로부터의 거리와 오른손으로부터의 거리를 구한다.
            l_distance = bfs(left, location[number])
            r_distance = bfs(right, location[number])
            # 왼손 거리가 더 가까울 경우
            # 왼손 좌표를 이동하고 정답에 L 추가
            if l_distance < r_distance:
                left = location[number]
                answer += 'L'
            # 오른손 거리가 더 가까울 경우
            # 오른손 좌표를 이동하고 정답에 R 추가
            elif l_distance > r_distance:
                right = location[number]
                answer += 'R'
            # 두 손의 거리가 똑같을 경우
            else:
                # 왼손잡이일 경우에는 왼손을 택하고, 오른손잡이일 경우에는 오른손을 택한다.
                if hand == 'left':
                    left = location[number]
                    answer += 'L'
                else:
                    right = location[number]
                    answer += 'R'

    return answer


# main
T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    hand = input()
    
    print("#{} {}".format(tc, solution(numbers, hand)))

