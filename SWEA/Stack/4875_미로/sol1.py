import sys
sys.stdin = open('sample_input.txt')


def dfs(graph, visit, idx, finish, result):
    visit[idx] = True
    if idx == finish:
        result[0] = 1
    for num in graph[idx]:
        if not visit[num]:
            dfs(graph, visit, num, finish, result)


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    maze = [[1] * (N+2)]
    for _ in range(N):
        maze.append([1] + list(map(int, list(input()))) + [1])
    maze.append([1] * (N+2))

    graph = [[] for _ in range(N**2 + 1)]
    idx = 1
    start = finish = -1

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if maze[i][j] == 2:
                start = idx
            if maze[i][j] == 3:
                finish = idx
            if maze[i-1][j] != 1:
                graph[idx].append(idx-N)
            if maze[i+1][j] != 1:
                graph[idx].append(idx+N)
            if maze[i][j-1] != 1:
                graph[idx].append(idx-1)
            if maze[i][j+1] != 1:
                graph[idx].append(idx+1)
            idx += 1

    if start == -1 or finish == -1:
        print('#{} {}'.format(tc, 'error'))
    else:
        result = [0]
        visit = [False] * (N**2 + 1)
        dfs(graph, visit, start, finish, result)
        print('#{} {}'.format(tc, result[0]))
