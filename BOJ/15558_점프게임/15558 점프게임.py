import sys
from collections import deque

def bfs(game, N, k):
    start = (0, 1, 0)
    queue = deque()
    queue.append(start)
    directions = [(0, 1), (0, -1), (1, k), (-1, k)]
    visit = [[False] * (N + 1) for _ in range(2)]
    visit[0][1] = True
    flag = False

    while queue:
        location = queue.popleft()
        for direction in directions:
            if location[0] == 0 and direction[0] == -1:
                continue
            if location[0] == 1 and direction[0] == 1:
                continue
            
            new_location = (location[0] + direction[0], location[1] + direction[1], location[2] + 1)
            
            if new_location[1] > N:
                flag = True
                break
            
            
            if game[new_location[0]][new_location[1]] != 0 and not visit[new_location[0]][new_location[1]]:
                visit[new_location[0]][new_location[1]] = True
                queue.append(new_location)
                
        game[0][new_location[2]] = 0
        game[1][new_location[2]] = 0
                    
        if flag:
            return 1
        
    return 0
        
# main
N, k = map(int, sys.stdin.readline().split())
game = [[0] + list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(2)]

start = game[0][1]
queue = deque((0, 1))

print(bfs(game, N, k))
