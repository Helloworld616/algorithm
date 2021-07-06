import sys
sys.stdin = open('input.txt')


def solution(G):
    visited = [False for _ in range(100)]
    to_visits = [0]

    while to_visits:
        now = to_visits.pop()
        # if now == 99:
        #     return 1
        if not visited[now]:
            visited[now] = True
            to_visits += G[now]

    return int(visited[99])


T = int(input())


for tc in range(1, T+1):
    tc , E = map(int, input().split())
    G = [[] for _ in range(100)]
    edge_list = list(map(int, input().split()))
    for idx in range(0, len(edge_list), 2):
        fr = edge_list[idx]
        to = edge_list[idx+1]
        G[fr].append(to)

    print("#{} {}".format(tc, solution(G)))
