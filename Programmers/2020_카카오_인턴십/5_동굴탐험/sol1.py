def dfs(idx, start, flag, tree, visited):
    visited[idx] = True
    # print(visited)
    for node in tree[idx]:
        if node == start:
            flag = False
        else:
            if not visited[node]:
                dfs(node, start, flag, tree, visited)


def solution(n, path, order):
    visited = [False] * n

    tree = [[] for _ in range(n)]
    predecessor = [0 for _ in range(n)]

    for road in path:
        tree[road[1]].append(road[0])
        tree[road[0]].append(road[1])

    for start, goal in order:
        if goal == 0:
            return False
        predecessor[goal].append(start)

    visited[0] = True
    for node in tree[0]:
        if not visited[node]:

    return False

print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))