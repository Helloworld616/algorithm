import sys


def plan(today, profit, schedule, profits):
    next_day = today + schedule[today][0]
    if next_day >= len(schedule)-1:
        if next_day == len(schedule)-1 and next_day + schedule[next_day][0] == len(schedule):
            profit += schedule[next_day][1]
            profits.append(profit)
            profit -= schedule[next_day][1]
        else:
            profits.append(profit)
    else:
        for day in range(next_day, len(schedule)):
            if day + schedule[day][0] <= len(schedule):
                profit += schedule[day][1]
                plan(day, profit, schedule, profits)
                profit -= schedule[day][1]    

N = int(sys.stdin.readline())
schedule = [0]
profit = 0
profits = []

for day in range(N):
    time, price = map(int, sys.stdin.readline().split())
    schedule.append((time, price))

for day in range(1, len(schedule)):
    if day + schedule[day][0] <= len(schedule):
        profit += schedule[day][1]
        plan(day, profit, schedule, profits)
        profit -= schedule[day][1]

if len(profits) == 0:
    print(0)
else: 
    max_profit = profits[0]
    for idx in range(1, len(profits)):
        if profits[idx] > max_profit:
            max_profit = profits[idx]
    print(max_profit)     
        
