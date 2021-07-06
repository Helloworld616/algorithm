import sys

def dfs(graph, visit, check, idx):
    visit[idx] = 1
    check[idx] = 1
    for i in range(len(graph[idx])):
        if visit[graph[idx][i]] == 0:
            dfs(graph, visit, check, graph[idx][i])


def town(graph, valid, n):
    town = []
    visit = [0 for _ in range(n*n + 1)]
    cnt = 0

    for i in range(1, n*n + 1):
        if visit[i] == 0 and valid[i] == 1:
            check = [0 for _ in range(n*n + 1)]
            dfs(graph, visit, check, i)
            town.append(check.count(1))
            cnt += 1
    town.sort()
    town.insert(0, cnt)

    return town



n = int(sys.stdin.readline())

area = []
blank1 = blank2 = [0 for _ in range(n+2)]
area.append(blank1)

for i in range(n):
    apart = list(map(int, list(sys.stdin.readline().rstrip())))
    apart.insert(0, 0)
    apart.append(0)
    area.append(apart)

area.append(blank2)

graph = [[] for _ in range(n*n + 1)]
valid = [[] for _ in range(n*n + 1)]
graph_index = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        if area[i][j] == 1:
            valid[graph_index] = 1
            if area[i-1][j] == 1:
                graph[graph_index].append(graph_index-n)
            if area[i+1][j] == 1:
                graph[graph_index].append(graph_index+n)
            if area[i][j-1] == 1:
                graph[graph_index].append(graph_index-1)
            if area[i][j+1] == 1:
                graph[graph_index].append(graph_index+1)
        graph_index += 1

town = town(graph, valid, n)

for num in town:
    print(num)

