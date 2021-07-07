import sys
import copy

sys.stdin = open("input.txt")
input = sys.stdin.readline

# CCTV의 감시 범위를 저장한 딕셔너리
infos = {
    1: [
        [(-1, 0)],
        [(1, 0)],
        [(0, -1)],
        [(0, 1)]
    ],
    2: [
        [(-1, 0), (1, 0)],
        [(0, -1), (0, 1)],
    ],
    3: [
        [(-1, 0), (0, 1)],
        [(1, 0), (0, 1)],
        [(1, 0), (0, -1)],
        [(-1, 0), (0, -1)]
    ],
    4: [
        [(-1, 0), (0, -1), (0, 1)],
        [(-1, 0), (1, 0), (0, 1)],
        [(1, 0), (0, -1), (0, 1)],
        [(-1, 0), (1, 0), (0, -1)]
    ],
    5: [
        [(-1, 0), (1, 0), (0, -1), (0, 1)]
    ]
}


# 사각지대의 갯수를 세는 함수
def count_blank(matrix):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not matrix[i][j]:
                cnt += 1

    return cnt


# 완전탐색 함수
# 완전탐색을 통해 모든 감시의 수를 체크해보자!
def watch(matrix, idx, counter):
    # idx가 리스트 cctv의 길이와 같을 경우 탐색 중지
    # 그 후 사각지대의 갯수를 세서 저장한다.
    if idx == len(cctv):
        counter.append(count_blank(matrix))
        return

    # CCTV 위치 정보 받기
    row, col = cctv[idx][0], cctv[idx][1]

    # 딕셔너리 infos에서 감시 범위를 가져와서
    # 모든 감시의 수를 체크해본다.
    for info in infos[matrix[row][col]]:
        n_matrix = copy.deepcopy(matrix)  # 인자로 받은 사무실 정보를 복사
        for delta in info:
            dr = delta[0]  # 행의 이동값
            dc = delta[1]  # 열의 이동값
            n_row = row + dr  # 이동한 행
            n_col = col + dc  # 이동한 열
            # 사무실 범위 내에서, 6을 만나지 않을 때까지 감시 실행
            while 0 <= n_row < N and 0 <= n_col < M and n_matrix[n_row][n_col] != 6:
                if not n_matrix[n_row][n_col] and n_matrix[n_row][n_col] != '#':
                    n_matrix[n_row][n_col] = '#'
                n_row += dr
                n_col += dc
        # 한 차례의 감시가 끝나면 다음 CCTV로 이동
        watch(n_matrix, idx + 1, counter)


# main

# 입력 받기
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cctv = []  # CCTV의 위치를 담을 리스트
counter = []  # 사각지대의 갯수를 담을 리스트

# 주어진 사무실 정보를 조회하여 cctv의 위치 파악하기
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j))

# 완전탐색 실시
watch(office, 0, counter)

# 최소의 사각지대 갯수를 출력
print(min(counter))
