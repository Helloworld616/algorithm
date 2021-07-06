# 다른 친구 코드 3

# 백트래킹: 넣을지 말지, 넣을 경우 현재까지의 합이 제한 칼로리를 넘지 않는지.
# 마지막 재료까지 전부 결정했다면 이전으로 돌아가기

def dfs(i):
    global max_t, now_t, now_k
    # 전체 재료 탐색 완료 시 종료; 점수 갱신 시 확인
    if i == N:
        if now_t > max_t:
            max_t = now_t
        return
    # 이번 재료 포함시 칼로리 한계 도달 + 점수 갱신 시
    if now_k + tks[i][1] > L:
        if now_t > max_t:
            max_t = now_t
    # 이번 재료 포함 시에도 칼로리 한계 도달 X
    else:
        # 이번 재료 포함하여 탐색
        now_t += tks[i][0]
        now_k += tks[i][1]
        dfs(i + 1)
        # 복구
        now_t -= tks[i][0]
        now_k -= tks[i][1]
    # 이번 재료 미포함
    dfs(i + 1)


T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    tks = [list(map(int, input().split())) for _ in range(N)]

    max_t = 0
    now_t = 0
    now_k = 0
    dfs(0)

    print('#{} {}'.format(tc, max_t))