import sys
sys.stdin = open('sample_input.txt')

# 상, 하, 좌, 우 4방향을 나타내는 리스트
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 탐색 함수
# number : 좌표 안의 숫자
# row : 행
# col : 열
# cnt : 자리 수
# result : 결과로 도출된 일곱 자리 수들을 담는 리스트
def move(number, row, col, cnt, result):
    if cnt == 6:
        """
        종료 조건 : cnt가 6이 될 때 
        (cnt를 0부터 시작했으므로, 6이 되는 순간이 자리 수가 7이 되는 순간이다!)
        """
        # 일곱 자리 수를 결과 리스트에 추가
        result_value = ''.join(number)
        result.append(result_value)
    else:
        """
        실행 조건 : cnt가 아직 6이 되지 않았을 때 
        """
        # 4방향 탐색을 실행
        for i in range(4):
            n_row = row + dr[i]
            n_col = col + dc[i]
            # 탐색 방향이 격자판의 범위에 있을 경우 다음 탐색 실행
            if 0 <= n_row < 4 and 0 <= n_col < 4:
                number.append(matrix[n_row][n_col])
                move(number, n_row, n_col, cnt + 1, result)
                number.pop()


# main
for tc in range(1, int(input())+1):
    # 격자판을 이차원 배열로 입력 받기
    matrix = [list(input().split()) for _ in range(4)]

    # 생성되는 일곱 자리 수를 담을 리스트 result 생성
    result = []
    # 격자판의 모든 좌표를 시작점으로 삼아 탐색
    for i in range(4):
        for j in range(4):
            move([matrix[i][j]], i, j, 0, result)

    # 중복을 제거한 result의 길이 출력
    print('#{} {}'.format(tc, len(set(result))))

