import sys

def dfs(result, record, cost, world, j, n):
    cost += world[record[-1]][j]
    if len(record) == n:
        result.append(cost)
    else:
        for idx in range(n):
            if world[j][idx] != 0:
                if len(record) == n-1 and idx == record[0]:
                    record.append(j)
                    dfs(result, record, cost, world, idx, n)
                    record.pop()
                else:
                    if idx not in record:
                        record.append(j)
                        dfs(result, record, cost, world, idx, n)
                        record.pop()



# main
n = int(sys.stdin.readline())
world = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    world.append(row)


result = []

for j in range(n):
    if world[0][j] != 0:
        dfs(result, [0], 0, world, j, n)

answer = result[0]
for i in range(1, len(result)):
    if result[i] < answer:
        answer = result[i]

print(answer)


        

