import sys
sys.stdin = open("sample_input.txt")

"""
문제 한 줄 요약 : 연결 요소의 갯수를 구하시오.
"""


# 재귀로 구현한 dfs 함수
def dfs(idx):
    visited[idx] = True
    for vertex in graph[idx]:
        if not visited[vertex]:
            dfs(vertex)


# main
T = int(input())

for tc in range(1, T+1):
    # 출석 번호, 신청서 매수, 그룹 정보 입력 받기
    N, M = map(int, input().split())
    group = list(map(int, input().split()))

    # 그래프와 방문 배열 생성 및 초기화
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    # 그룹 정보를 보고 그래프(인접 리스트)를 생성.
    # 양방향 그래프 이므로 양쪽 사람 모두 정보를 추가!
    for i in range(0, len(group)-1, 2):
        graph[group[i]].append(group[i+1])
        graph[group[i+1]].append(group[i])

    # 연결 요소 갯수 구하기
    # 갯수를 0으로 초기화
    cnt = 0
    # dfs 탐색을 하면서, dfs가 끝날 때마다 갯수를 1 증가시킴
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    # 최종적으로 산출된 연결 요소의 갯수 출력
    print("#{} {}".format(tc, cnt))
