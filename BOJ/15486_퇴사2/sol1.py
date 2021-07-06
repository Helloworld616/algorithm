import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
time = [0]
profit = [0]
inc = [0] * (N + 1)

for _ in range(N):
    T, P = map(int, sys.stdin.readline().split())
    time.append(T)
    profit.append(P)

for i in range(1, N+1):
    if inc[i - 1] > inc[i]:
        inc[i] = inc[i-1]
    if i + time[i] <= N and profit[i] + inc[i] > inc[i + time[i]]:
        inc[i + time[i]] = profit[i] + inc[i]


for i in range(1, N+1):
    if i + time[i] <= N+1:
        profit[i] += inc[i]
    else:
        profit[i] = 0


max_profit = profit[0]
for i in range(1, N+1):
    if profit[i] > max_profit:
        max_profit = profit[i]

print(max_profit)

