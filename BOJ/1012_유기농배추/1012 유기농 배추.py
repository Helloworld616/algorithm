import sys


# dfs 함수. 스택으로 구현
def dfs(graph, visit, idx):
    to_visit = [idx]

    while to_visit:
        current = to_visit.pop()
        if not visit[current]:
            visit[current] = True
            to_visit += graph[current]
            

# 연결요소의 갯수 구하는 함수
def component(graph, valid):
    visit = [False]*(len(graph)+1)
    component = 0
    
    for idx in range(1, len(graph)):
        if valid[idx] and not visit[idx]:
            dfs(graph, visit, idx)
            component += 1

    return component


# main
# 케이스 갯수 입력받기
T = int(sys.stdin.readline())
# 상화좌우 체크를 위해 만든 리스트 directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    # M, N, K를 입력받고 이차원리스트 garden 생성
    M, N, K = map(int, sys.stdin.readline().split())
    garden = [[0]*(M+2) for _ in range(N+2)]

    # X, Y 위치의 garden 값을 1로 변경
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        garden[Y+1][X+1] = 1

    # 그래프와 유효성 검사할 리스트 valid 생성
    graph = [[] for _ in range((M*N)+1)]
    valid = [False for _ in range((M*N)+1)]
    idx = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            # garden[i][j]에 값이 있을 경우 valid를 True로 변경
            # 이후 상하좌우 값을 검사해서 1이 있을 경우 그래프에 좌표 추가
            if garden[i][j]:
                valid[idx] = True
                for direction in directions:
                    if garden[i+direction[0]][j+direction[1]]:
                        if not direction[0]:
                            graph[idx].append(idx + direction[1])
                        else:
                            graph[idx].append(idx + direction[0]*M)
            idx += 1

    print(component(graph, valid))
                        
    
        
    
    
