"""
왜 완전탐색 파트에 있는지 정말 알 수 없는 문제입니다...

엄청 유명한 DP 문제여서 Dynamic Programming으로 풀었습니다.
케이스가 완전탐색 유효범위인 10을 넘어가는 것을 보고 완전탐색은 바로 버렸습니다.

근데 문제에서는 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다고 나와있는데...
시간 초과 받으라고??? -_-;;;

물론 백트래킹으로 할 수야 있겠지만 너무 귀찮아서... 훨씬 간단한 방법인 DP를 택했습니다.

"""

import sys
sys.stdin = open('sample_input.txt')


for tc in range(1, int(input())+1):
    # N과 숫자판 입력 받기
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 dp 배열 생성. 모두 0으로 초기화
    dp = [[0 for _ in range(N)] for _ in range(N)]

    # Base Case 채워넣기 1 : matritx의 (0, 0) 값을 dp 배열의 (0, 0) 인덱스에 넣습니다.
    dp[0][0] = matrix[0][0]
    # Base Case 채워넣기 2 : dp와 matrix의 합산 값으로 dp의 기본 값들(왼쪽, 위쪽 테두리)을 채웁니다.
    for i in range(1, N):
        dp[0][i] = dp[0][i-1] + matrix[0][i]
        dp[i][0] = dp[i-1][0] + matrix[i][0]

    # 연산 수행
    # 출발지에서 오른쪽이나 아래로만 이동할 수 있으므로, 도착지에서는 왼쪽이나 위에서만 이동을 받게 됩니다.
    # 따라서 왼쪽에서 오는 값과 위에서 오는 값 중 더 작은 값을 선택해 matrix 배열의 값에 더해주면 됩니다.
    for i in range(1, N):
        for j in range(1, N):
            dp[i][j] = matrix[i][j] + min(dp[i-1][j], dp[i][j-1])

    # 이 과정을 거쳐 dp 배열의 도착지 지점에는 최솟값이 저장됩니다.
    # 그 값을 출력합니다.
    print('#{} {}'.format(tc, dp[N-1][N-1]))
