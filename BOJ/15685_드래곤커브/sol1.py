import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# 좌표를 모두 미방문 상태로 초기화
matrix = [[False] * 101 for _ in range(101)]
# 커브 변환 결과를 나타내는 딕셔너리
transform = {0: 1, 1: 2, 2: 3, 3: 0}
# 상하좌우 4방향을 나타내는 리스트
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

# 드래곤 커브 갯수 입력 받기
N = int(input())

# 입력 받는 커브 갯수만큼 반복문 실행
for _ in range(N):
    # 입력 받기
    x, y, d, g = map(int, input().split())
    # 첫 번째 이동 좌표 계산
    ny, nx = y + dr[d], x + dc[d]

    # 방향을 저장하는 리스트
    direction = [d]
    # 첫 번째 이동 결과 방문한 좌표들을 방문 처리
    matrix[y][x] = True
    matrix[ny][nx] = True

    # 다음 세대 커브 만들기
    for _ in range(g):
        # 현재 방향의 갯수를 미리 저장
        length = len(direction) - 1

        # transform 딕셔너리를 참고해, 다음 커브 방향을 저장한다.
        for i in range(length, -1, -1):
            direction.append(transform[direction[i]])

        # 다음 커브 방향들이 다 산출되었으면
        # 그대로 이동해서 다음 세대의 드래곤 커브를 만든다.
        for i in range(length + 1, len(direction)):
            ny += dr[direction[i]]
            nx += dc[direction[i]]
            matrix[ny][nx] = True

# 사각형의 갯수를 0으로 초기화
cnt = 0
# 좌표들을 탐색해서, 1 X 1 사각형의 4개 좌표가 모두 방문처리 되었으면 cnt 1 증가
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
            cnt += 1

# cnt 출력
print(cnt)
