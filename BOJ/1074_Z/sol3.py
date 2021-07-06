import sys
sys.stdin = open('input.txt')

# 입력 받기
N, r, c = map(int, input().split())

# 방향을 나타내는 리스트 생성
# 제자리, 오른쪽, 좌측 아래, 우측 아래
dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]

power = 2**(N-1) # 좌표의 증가분을 나타내는 제곱수
plus = 4**(N-1) # 방문 번호의 증가분
row = 0 # 행
col = 0 # 열
start = 0 # 맨 처음 방문 번호

# 제곱수가 1이 될 때까지 반복문 수행
while power != 1:
    # 다음으로 이동할 좌표의 후보군을 담을 리스트 생성
    candidates = []
    # 4방향 탐색
    for i in range(4):
        # 현재 방향에서 제곱수만큼 이동한 좌표 지점을 저장
        n_row = row + dr[i] * power
        n_col = col + dc[i] * power
        # 새로운 시작 지점을 계산해서 저장
        n_start = start + i * plus

        # 새로운 좌표가 r과 c 이하일 경우 (r과 c보다 크면 r과 c를 포함하지 못함)
        if n_row <= r and n_col <= c:
            # 다음으로 이동할 좌표와 시작점의 후보군에 담는다.
            candidates.append((n_row, n_col, n_start))

    # 후보군들 중에서 가장 나중에 있는 것을 다음 좌표와 다음 시작점에 저장한다.
    # 가장 나중에 있는 것이 r과 c와 가깝기 때문
    row = candidates[-1][0]
    col = candidates[-1][1]
    start = candidates[-1][2]

    # 좌표 증가분을 2로 나누고
    # 방문번호 증가분을 4로 나눈다.
    power //= 2
    plus //= 4

# 탐색하면서 r과 c와 일치하는 지점을 찾는다.
for i in range(4):
    n_row = row + dr[i]
    n_col = col + dc[i]
    # 찾았을 경우 그 지점의 번호를 출력하고 프로그램 종료
    if n_row == r and n_col == c:
        print(start)
        sys.exit(0)
    # 찾지 않았을 경우 지점 번호를 1 증가
    # 다음 지점으로 이동하면 번호가 1 증가하기 때문
    start += 1



