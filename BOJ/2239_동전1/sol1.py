import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
dp = [1] + [0] * K
coin = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(N):
    for j in range(1, K+1):
        if coin[i] <= j:
            dp[j] += dp[j - coin[i]]

print(dp[K])

