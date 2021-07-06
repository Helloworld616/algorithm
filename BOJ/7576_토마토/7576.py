import sys
from collections import deque

def bfs(box, queue):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        space = queue.popleft()
        for direction in directions:
            new_row = space[0] + direction[0] 
            new_col = space[1] + direction[1]
            if box[new_row][new_col] == 0:
                box[new_row][new_col] = box[space[0]][space[1]] + 1
                queue.append((new_row, new_col))

    return box


# main
n, m = map(int, sys.stdin.readline().split())
box = []
dummy1 = dummy2 = [-2 for _ in range(n+2)]
box.append(dummy1)

for _ in range(m):
    box_row = list(map(int, sys.stdin.readline().rstrip().split()))
    box_row.insert(0, -2)
    box_row.append(-2)
    box.append(box_row)

box.append(dummy2)

queue = deque()

for i in range(1, m+1):
    for j in range(1, n+1):
        if box[i][j] == 1:
            queue.append((i, j))

result = bfs(box, queue)

count = 0
max_day = 0
for i in range(1, m+1):
    for j in range(1, n+1):
        if result[i][j] > max_day:
            max_day = result[i][j]
        if result[i][j] == 0:
            count += 1

if count > 0:
    print(-1)
else:
    print(max_day-1)