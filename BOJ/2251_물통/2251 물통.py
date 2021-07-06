import sys
from collections import deque


def bfs(check, capacity):
    start = [0, 0, capacity[2]]
    directions = [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    visit = []
    queue = deque()
    queue.append(start)
    visit.append(start)

    while queue:
        ready = queue.popleft() 
        for direction in directions:
            water = ready[:]
            if capacity[direction[1]] - water[direction[1]] <= water[direction[0]]:
                water[direction[0]] -= capacity[direction[1]] - water[direction[1]]
                water[direction[1]] = capacity[direction[1]]
            else:
                water[direction[1]] += water[direction[0]]
                water[direction[0]] = 0
            if water[0] == 0:
                check[water[2]] += 1
            if water not in visit:
                queue.append(water)
                visit.append(water)
                

capacity = list(map(int, sys.stdin.readline().split()))
check = [0 for _ in range(capacity[2]+1)]
check[capacity[2]] += 1

bfs(check, capacity)

result = []
for idx in range(len(check)):
    if check[idx] > 0:
        result.append(idx)

print(' '.join(map(str, result)))
