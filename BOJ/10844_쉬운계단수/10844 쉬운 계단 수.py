import sys

N = int(sys.stdin.readline())

stair = [[1]*9]

for i in range(N-1):
    stair.append([0]*9)

for i in range(1, N):
    stair[i][8] = stair[i-1][7]
    for j in range(7, 0, -1):
        stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]
    stair[i][0] = stair[i][7]

answer = 0
for i in range(len(stair[N-1])):
    answer += stair[N-1][i] % 1000000000

print(answer % 1000000000)
