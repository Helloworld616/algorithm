import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 입력 받아 미로와 dp 생성
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]

# dp 초기화
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + maze[0][i]

for i in range(1, N):
    dp[i][0] = dp[i-1][0] + maze[i][0]

# dp 계산
for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = max(maze[i][j] + dp[i-1][j], maze[i][j] + dp[i][j-1], maze[i][j] + dp[i-1][j-1])

# 도찾지의 값 출력
print(dp[N-1][M-1])