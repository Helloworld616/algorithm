import sys
sys.stdin = open('input.txt')


def MAX(A, B):
    if A > B:
        return A
    else:
        return B

# main
N = int(sys.stdin.readline())
wine = [0] + [int(sys.stdin.readline()) for _ in range(N)]
dp = [0] * (N+1)

if N == 1:
    print(wine[1])

elif N == 2:
    print(wine[1] + wine[2])

else:
    for i in range(1, 3):
        dp[i] = wine[i]
        dp[i] += dp[i-1]

    for j in range(3, N+1):
        dp[j] = MAX(dp[j-2] + wine[j], dp[j-3] + wine[j-1] + wine[j])
        dp[j] = MAX(dp[j], dp[j-1])

    print(dp[N])