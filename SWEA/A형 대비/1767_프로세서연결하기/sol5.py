# 성공
# 시간 : 642ms

import sys
sys.stdin = open('sample_input.txt')

'''

백트래킹 문제!

1. 코어의 좌표를 저장한다. 이 때 가장자리의 코어는 제외한다. (가장자리의 코어는 이미 연결되어 있으므로)
2. 각 코어의 상하좌우를 탐색하여 연결 가능 여부를 체크하여 저장한다.
3. 코어의 최대값(max_cnt)과 길이의 최소값(min_len)을 초기화한다. max_cnt는 0, min_len은 987654321로 초기화
4. 첫 좌표부터 마지막 좌표까지 백트래킹 실시. 백트래킹 가능 조건은 다음과 같다.
   (1) 현재 연결하려는 코어와 남아있는 코어의 합이 max_cnt 보다 크거나 같아야 한다.
   (2) 현재 연결하려는 코어와 남아있는 코어의 합이 max_cnt와 같을 경우 현재 길이는 min_len보다 작아야 한다.
4. 연결하지 않은 경우를 백트래킹으로 넘긴다. 연결하지 않은 경우도 비교해야 하기 때문이다.
6. 다음은 연결한 경우. 유망한 좌표들의 상하좌우 4방향을 탐색한다. 탐색 가능 조건은 다음과 같다.
   (1) 연결 가능한 방향이어야 한다. (2번에서 저장한 정보를 활용)
   (2) 좌표의 행과 열은 0 이상 N 미만이어야 한다.
   (3) 이전에 탐색한 좌표는 탐색할 수 없다.
6. 5번의 탐색을 거쳐서 연결이 완료된 경우 다음 단계로 넘어간다.
7. 상기의 과정을 거쳐 연결 갯수가 max_cnt보다 클 경우 max_cnt와 min_len을 갱신
8. 연결 갯수가 max_cnt와 같고 길이가 min_len보다 작을 경우 min_len 갱신
9. 최종적으로 산출된 min_len 출력

'''


# 백트래킹 함수
def charge(cnt, min_len, max_cnt, idx, length, record):
    # cores의 인덱스가 cores의 길이과 같아질 때
    if idx == len(cores):
        # cnt가 max_cnt보다 클 때 max_cnt, min_len 갱신
        if cnt > max_cnt[0]:
            max_cnt[0] = cnt
            min_len[0] = length
        # cnt가 max_cnt와 같을 때, length가 min_len보다 작다면 min_len 갱신
        elif cnt == max_cnt[0]:
            if length < min_len[0]:
                min_len[0] = length
    # cores의 인덱스가 cores의 길이보다 작을 때
    else:
        # 다음 두 가지 경우에만 실행
        # 1. 현재 연결하려는 코어와 남아있는 코어의 합이 max_cnt 보다 클 때
        # 2. 현재 연결하려는 코어와 남아있는 코어의 합이 max_cnt와 같고 현재 길이는 min_len보다 작을 때
        if cnt + len(cores) - idx > max_cnt[0] or (cnt + len(cores) - idx == max_cnt[0] and length < min_len[0]):
            # 연결하지 않은 상태에서 다음 백트래킹 진행
            charge(cnt, min_len, max_cnt, idx + 1, length, record)
            # core의 좌표로부터 상하좌우 탐색 후, 연결이 가능하면 다음 백트래킹 진행
            for i in range(4):
                if checks[idx][i]:
                    # row는 현재 방향으로 나아갈 때의 행 좌표
                    # col은 현재 방향으로 나아갈 때의 열 좌표
                    row = cores[idx][0] + dr[i]
                    col = cores[idx][1] + dc[i]
                    # letmp는 현 상황에서 연결했을 때의 길이
                    # rtemp는 현 상황에서 연결한 좌표들
                    ltemp = 0
                    rtemp = []
                    # row와 col이 0 이상 N 미만이고 이전의 탐색 기록에 없을 경우에 탐색 진행
                    while 0 <= row < N and 0 <= col < N and (row, col) not in set(record):
                        ltemp += 1
                        rtemp.append((row, col))
                        row += dr[i]
                        col += dc[i]
                    # row와 col이 끝까지 갔다면 다음 백트래킹 진행
                    if row < 0 or col < 0 or row == N or col == N:
                        charge(cnt + 1, min_len, max_cnt, idx + 1, length + ltemp, record + rtemp)


# main
T = int(input())

for tc in range(1, T+1):
    # 입력 받아 matrix 생성
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 방향을 나타내는 리스트
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # core가 위치한 좌표들 저장
    cores = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if matrix[i][j] == 1:
                cores.append((i, j))

    # cores 안의 좌표들을 하나씩 꺼내서 상하좌우 탐색
    # 끝까지 가서 충전할 수 있으면 True, 중간에 막힌다면 False 저장
    checks = []
    for core in cores:
        check = []
        for i in range(4):
            row = core[0] + dr[i]
            col = core[1] + dc[i]
            while 0 <= row < N and 0 <= col < N and matrix[row][col] == 0:
                row += dr[i]
                col += dc[i]
            if row < 0 or col < 0 or row == N or col == N:
                check.append(True)
            else:
                check.append(False)
        checks.append(check)

    # max_cnt, min_len 초기화
    max_cnt = [0]
    min_len = [987654321]

    # 백트래킹 함수 호출
    charge(0, min_len, max_cnt, 0, 0, [])

    # min_len 출력
    print('#{} {}'.format(tc, min_len[0]))