import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 함수
# row : 비용을 담은 이차원 리스트의 행
# result : 비용 계산 결과
def cal(row, result):
    global ans

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
            # 비용을 더한다
            result += cost[row][i]
            # 아직 i번쨰 공작을 방문하지 않았고, result가 ans보다 작을 경우
            # 방문 체크를 하고 다음 백트래킹 실시
            if not visit[i] and result < ans:
                visit[i] = True
                cal(row+1, result)
                visit[i] = False
            # 비용 계산 결과를 다시 원래대로 돌려놓는다.
            result -= cost[row][i]


# main
T = int(input())

for tc in range(1, T+1):
    # 제품의 종류와 비용 입력 받기
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    # 방문 배열과 정답의 초기값 생성
    visit = [False] * N
    ans = float('inf')

    # 백트래킹 실시
    cal(0, 0)

    # 정답 출력
    print('#{} {}'.format(tc, ans))
