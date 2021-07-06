import sys

N = int(sys.stdin.readline())
schedule = []
profit = [0] * N

for day in range(N):
    time, price = map(int, sys.stdin.readline().split())
    schedule.append((time, price))

for i in range(N):
    if i + schedule[i][0] <= N:
        profit[i] = schedule[i][1]
        initial_profit = profit[i]
        for j in range(i):
            if j + schedule[j][0] <= i and profit[i] < initial_profit + profit[j]:
                profit[i] = initial_profit + profit[j]

max_profit = profit[0]
for i in range(1, len(profit)):
    if profit[i] > max_profit:
        max_profit = profit[i]
        
print(max_profit)
