import sys
from collections import deque

def bfs(graph, start, finish):
    visited = [0 for _ in range(finish+1)]
    distance = [0 for _ in range(finish+1)]
    queue = deque([start])
    distance[start] += 1

    while queue:
        road = queue.popleft()
        for location in graph[road]:
            if visited[location] == 0:
                visited[location] = 1
                queue.append(location)
                distance[location] = distance[road] + 1
        
    return distance[finish]


# main
n, m = map(int, sys.stdin.readline().split())
maze = []
dummy1 = dummy2 = [0 for _ in range(m+2)]
maze.append(dummy1)

for _ in range(n):
    maze_row = list(map(int, list(sys.stdin.readline().rstrip())))
    maze_row.insert(0, 0)
    maze_row.append(0)
    maze.append(maze_row)

maze.append(dummy2)
graph = {}
graph_index = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if maze[i][j] == 1:
            if maze[i-1][j] == 1:
                if graph_index not in graph:
                    graph[graph_index] = [graph_index-m] 
                else:
                    graph[graph_index].append(graph_index-m)
            if maze[i+1][j] == 1:
                if graph_index not in graph:
                    graph[graph_index] = [graph_index+m]
                else:
                    graph[graph_index].append(graph_index+m)
            if maze[i][j-1] == 1:
                if graph_index not in graph:
                    graph[graph_index] = [graph_index-1] 
                else:
                    graph[graph_index].append(graph_index-1)
            if maze[i][j+1] == 1:
                if graph_index not in graph:
                    graph[graph_index] = [graph_index+1]
                else:
                    graph[graph_index].append(graph_index+1)
        graph_index += 1

print(bfs(graph, 1, n*m))