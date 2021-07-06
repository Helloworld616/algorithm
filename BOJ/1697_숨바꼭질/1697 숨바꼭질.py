import sys
from collections import deque

def bfs(queue, visit, K):
    directions = [-1, 1, 2]

    while queue:
        location = queue.popleft()
        for direction in directions:
            if direction == 2:
                new_location = location[0] * direction
            else:
                new_location = location[0] + direction

            second = location[1] + 1
            
            if new_location == K:
                return second
            else:
                if 0 <= new_location and new_location <= 200000:
                    if not visit[new_location]:
                        queue.append((new_location, second))
                        visit[new_location] = 1
                
# main
N, K = map(int, sys.stdin.readline().split())

if K <= N:
    answer = N - K
else:
    queue = deque()
    queue.append((N, 0))
    visit = [0] * 200001
    visit[N] = 1
    answer = bfs(queue, visit, K)

print(answer)

