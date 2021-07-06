import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
< 점화식 >

dp[i] = 2 * dp[i-1] + 시그마(dp[j] * dp[i-j-2] | j는 1부터 i-2까지의 정수)

'''


while True:
    # 입력 받기
    N = int(input())

    # 입력으로 들어오는 숫자가 0이면 종료
    if N == 0:
        sys.exit(0)

    # dp 배열 생성 및 초기화
    # 1로 초기화하는 이유는 첫 번째 base case인 dp[0]이 1 이기 때문!
    dp = [1] * N

    # N이 1보다 클 경우
    if N > 1:
        # 두 번째 base case 채우기
        # dp[1]은 2
        dp[1] = 2

        # N이 3이상일 때부터 점화식 반영
        # 점화식을 순차적으로 반영하고 결과값을 dp에 넣는다.
        for i in range(2, N):
            medicine = 2 * dp[i - 1]
            for j in range(i-1):
                medicine += dp[j] * dp[i-j-2]
            dp[i] = medicine

    # 결과 출력
    print(dp[N-1])