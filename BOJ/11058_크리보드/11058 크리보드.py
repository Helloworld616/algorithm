import sys

def max_num(candidate):
    max_num = candidate[0]
    for i in range(1, len(candidate)):
        if max_num < candidate[i]:
            max_num = candidate[i]
    return max_num


N = int(sys.stdin.readline())
dp = [i for i in range(7)]

for i in range(7, N+1):
    candidate = []
    for j in range(3, 8):
        candidate.append(dp[i-j] * (j - 1))
    dp.append(max_num(candidate))

print(dp[N])
        
