# 라이브강의 해설
import sys

sys.stdin = open('sample_input.txt')


def BFS(sV):
    # 큐를 생성과 동시에 선언
    Q = [sV]
    # 방문체크를 위한 배열 선언
    visited = [False] * (V + 1)
    visited[sV] = True

    dist = 0
    while Q:
        size = len(Q)

        for i in range(size):
            v = Q.pop(0)
            if v == eV:
                return dist

            for i in range(1, V+1):
                if not visited[i] and adj_arr[v][i]:
                    Q.append(i)
                    visited[i] = True
        dist += 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 정점의 수 1번부터 시작, E: 간선의 수

    # 인접행렬을 이용하여 작성해보자
    adj_arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        a, b = map(int, input().split())
        # 무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    # 시작점, 끝점
    sV, eV = map(int, input().split())

    print('#{} {}'.format(tc, BFS(sV)))