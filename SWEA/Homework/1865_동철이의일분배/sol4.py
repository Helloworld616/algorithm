import sys
# sys.stdin = open('input - 복사본.txt')
sys.stdin = open('input.txt')


# 백트래킹 함수
# row : 확률을 담은 이차원 리스트의 행
# visited : 방문 배열
def distribute(row, visited):
    global ans, result

    if row == N:
        """
        종료조건 : 행이 N과 같을 경우
        """
        # result가 ans보다 작은 상태를 유지하면서 끝까지 온 것이므로
        # ans를 더 작은 result로 교체
        ans = result
    else:
        """
        실행조건 : 아직 행이 N보다 작을 경우
        """
        # 0부터 (N-1)까지의 숫자들을 차례차례 꺼낸다.
        for i in range(N):
            # 백트래킹 조건 1
            # 아직 i번쨰 사람을 체크하지 않았고
            # i번째 사람의 확률이 0이 아닌 경우
            if not visited[i] and percent[row][i]:
                # 확률 계산
                result *= percent[row][i]
                # 백트래킹 조건 2
                # 계산한 확률이 현재 정답보다 클 경우에만 다음 탐색 실시
                if result > ans:
                    visited[i] = True
                    distribute(row + 1, visited)
                    visited[i] = False
                # 확률을 원래대로 되돌려놓기
                result /= percent[row][i]


# main
for tc in range(1, int(input()) + 1):
    # 직원의 수와 확률 입력 받기
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]

    # 확률 정보를 담은 이차원 리스트 percent 전처리
    # 탐색 비용을 줄이기 위해 미리 백분율로 바꾸어놓는다!
    for i in range(N):
        for j in range(N):
            percent[i][j] = percent[i][j] / 100

    # 정답, 확률 계산 결과, 방문 배열 초기화
    ans = 0
    result = 1
    visited = [False] * N

    # 백트래킹 실시
    distribute(0, visited)

    # 결과 출력
    # 역시 탐색 비용을 줄이기 위해 round 연산을 맨 마지막에 수행해준다!
    print('#%d %.6f' % (tc, round(ans * 100, 6)))
