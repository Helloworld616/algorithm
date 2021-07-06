import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


# 동쪽으로 이동했을 때의 주사위 변화
def move_to_east():
    temp1, temp2, temp3, temp4 = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = temp4, temp1, temp2, temp3


# 서쪽으로 이동했을 때의 주사위 변화
def move_to_west():
    temp1, temp2, temp3, temp4 = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
    dice[1][0], dice[1][1], dice[1][2], dice[3][1] = temp2, temp3, temp4, temp1


# 북쪽으로 이동했을 때의 주사위 변화
def move_to_north():
    temp1, temp2, temp3, temp4 = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = temp2, temp3, temp4, temp1


# 남쪽으로 이동했을 때의 주사위 변화
def move_to_south():
    temp1, temp2, temp3, temp4 = dice[0][1], dice[1][1], dice[2][1], dice[3][1]
    dice[0][1], dice[1][1], dice[2][1], dice[3][1] = temp4, temp1, temp2, temp3


# main
# 입력 받기
N, M, x, y, K = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
command = list(map(int, input().split()))

# 주사위 초기화. 처음에는 모든 면이 0이다!
dice = [[0] * 3 for _ in range(4)]
# 상하좌우 4방향을 나타내는 리스트
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
# 시작점 설정 (반드시 주어진 시작점을 활용하자! 안 그러면 틀림!)
row, col = x, y

# 명령어에서 숫자들을 하나씩 꺼낸다.
for number in command:
    # 숫자가 의미하는 방향으로 이동
    n_row = row + dr[number - 1]
    n_col = col + dc[number - 1]

    # 이동 범위가 지도의 좌표 범위 안일 경우에만 이동 가능!
    if 0 <= n_row < N and 0 <= n_col < M:
        # 다음 좌표 저장
        row, col = n_row, n_col

        # 숫자에 따라 이동
        if number == 1:
            move_to_east()
        if number == 2:
            move_to_west()
        if number == 3:
            move_to_north()
        if number == 4:
            move_to_south()

        # 필드가 0이 아닐 경우
        # 필드의 숫자를 주사위 아랫면에 넣고
        # 필드의 숫자를 0으로 변경
        if field[row][col] != 0:
            dice[3][1] = field[row][col]
            field[row][col] = 0
        # 필드가 0이 아닐 경우
        # 주사위 아랫면의 숫자를 필드에 복사
        else:
            field[row][col] = dice[3][1]

        # 주사위 윗면을 출력
        print(dice[1][1])
