import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    cost = list(map(int, input().split()))
    plan = [0, 0, 0] + list(map(int, input().split()))
    dp = [0] * 15

    for i in range(3, 15):
        dp[i] = min(dp[i-1] + cost[0] * plan[i], dp[i-1] + cost[1], dp[i-3] + cost[2], cost[3])

    print('#{} {}'.format(tc, dp[14]))

